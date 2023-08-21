#######################################
#        Windows environment          #
#######################################

## Create a virtual environment and install dependencies
win-install:
	python -m venv .wvenv
	.\.wvenv\Scripts\python.exe -m pip install --upgrade pip
	.\.wvenv\Scripts\python.exe -m pip install -r .\requirements.txt
	"$(get-location)" > .\.wvenv\Lib\site-packages\amygo.pth

## Run the development files
win-run: win-gen-ui win-gen-resources
	.\.wvenv\Scripts\python.exe .\main.py

## Remove development environment
win-clean:
	rm -r .\.wvenv\
	rm -r .\build
	rm -r .\dist

# Generate UI from Qt Designer files
win-gen-ui:
	.\.wvenv\Scripts\pyside6-uic.exe ./amygo/ui_main_window.ui -o ./amygo/ui_main_window.py --absolute-imports -python-paths .

# Generate embedded resources from Qt resource file
win-gen-resources:
	.\.wvenv\Scripts\pyside6-rcc.exe ./amygo/resources.qrc -o ./amygo/resources_rc.py

## Generate a production build
win-build:
	.\.wvenv\Scripts\pyinstaller.exe --noconfirm .\Amygo.spec
	md .\bundle
	Compress-Archive -Force -Path "./dist/Amygo/" -DestinationPath "bundle/Amygo.zip"

#######################################
#          Unix environment           #
#######################################

## Create a virtual environment and install dependencies
unix-install:
	python3 -m venv .venv
	.venv/bin/pip3 install --upgrade pip
	.venv/bin/pip3 install -r requirements.txt
	$(foreach dir, $(wildcard .venv/lib/*), echo $(shell pwd) > $(dir)/site-packages/amygo.pth &&) echo

## Run the development files
unix-run: unix-gen-ui unix-gen-resources
	.venv/bin/python3 ./main.py

## Remove development environment
unix-clean:
	rm -rf .venv

# Generate UI from Qt Designer files
unix-gen-ui:
	./.venv/bin/pyside6-uic ./amygo/ui_main_window.ui -o ./amygo/ui_main_window.py --absolute-imports -python-paths .

# Generate embedded resources from Qt resource file
unix-gen-resources:
	./.venv/bin/pyside6-rcc ./amygo/resources.qrc -o ./amygo/resources_rc.py

## Generate a production build
unix-build:
	./.venv/bin/pyinstaller --noconfirm ./DotaNotes.spec

