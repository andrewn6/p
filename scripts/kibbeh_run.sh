cd packages/kibbeh 


if [[ $1 != "-"*"i"* ]]
then
    echo Installing requirements...
    pip install -r requirements.txt
else
    echo Skipped installing requirements
fi

python main.py