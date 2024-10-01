SET BASE_PATH=%CD%

cd .venv/Scripts/
call activate

cd %BASE_PATH%

call python app/__main__.py