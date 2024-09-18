if not exist .venv/ (
    python -m venv .venv
)
SET BASE_PATH=%CD%

cd .venv/Scripts/
call activate

cd %BASE_PATH%
call python -m pip install --upgrade pip
call pip install -r requirements.txt

call python app/scripts/init.py
