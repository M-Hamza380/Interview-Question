import uvicorn, os, aiofiles, time, csv
from fastapi import FastAPI, File, Form, Request, Response, HTTPException, UploadFile, Depends
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.concurrency import run_in_threadpool


from src.pipeline.llm_pipeline import LLMPipeline

start_process = time.process_time()
print(f"Start process time: {start_process} seconds")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload(request: Request, file: UploadFile = File(...), filename: str = Form(...)):
    try:
        print(f"Received file: {file}, filename: {filename}")
        base_folder = "dataset/"
        if not os.path.isdir(base_folder):
            os.makedirs(base_folder, exist_ok=True)

        pdf_filename = os.path.join(base_folder, filename)

        # Read the file content from UploadFile
        file_content = await file.read()

        async with aiofiles.open(pdf_filename, "wb") as pdf_file:
            await pdf_file.write(file_content)

        # Confirm file has been written
        if not os.path.exists(pdf_filename):
            raise HTTPException(status_code=500, detail="File not found after upload")

        # Directly return the JSON response without manually encoding it
        print(f"Uploaded file size: {len(file_content)} bytes")
        return {"msg": "success", "pdf_filename": f"dataset/"}

    except Exception as e:
        print(f"Error during file upload: {e}")  # Log the error
        raise HTTPException(status_code=500, detail=f"Error occurred while uploading file: {str(e)}")

def get_csv():
    answer_chain, questions_list = LLMPipeline().run_llm_pipeline()
    print(f"Total Questions: {questions_list}")
    base_folder = "static/result/"
    if not os.path.isdir(base_folder):
        os.makedirs(base_folder, exist_ok=True)
    
    result_file = base_folder + "result.csv"
    with open(result_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Question', 'Answer'])
        # Generate answers for each question
        for question in questions_list:
            print("-"*50)
            print(f"Question: {question}")
            print("-"*50)
            answer = answer_chain.run(question)
            print(f"Answer: {answer}\n")
            print("-"*50)
            csv_writer.writerow([question, answer])
    return result_file

@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = f"static/result/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type='text/csv', filename=filename)
    else:
        raise HTTPException(status_code=404, detail="File not found")


@app.post("/analyze")
async def analyze(request: Request, pdf_filename: str = Form(...)):
    try:
        print(f"PDF Filename: {pdf_filename}")
        llm_pipeline = LLMPipeline()
        llm_pipeline.set_copy_data_dir(pdf_filename)
        output_file = await run_in_threadpool(lambda: get_csv())
        return{"output_file": output_file}
    except Exception as e:
        print(f"Error in analyze route: {e}")
        raise HTTPException(status_code=500, detail=f"Pipeline error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8080, reload=True)
    print(f"Process took {time.process_time() - start_process} seconds")
    