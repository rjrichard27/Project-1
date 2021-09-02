from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Calulate your BMI using your height (in inches) and weight (in lbs). Enter your height first then your weight"}

@app.get("/bmi/{height}/{weight}")
async def bmi(height: int, weight: int):
    """Calculates BMI"""

    BMI = (703 * weight) // (height**2)
    return {"BMI": BMI}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')