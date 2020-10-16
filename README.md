# What is WeightCalcTool?<br>
WeightCalcTool is a tool that can calculate your weight.
# Requirements
Python with Tkinter is required to run the code. Alternatively, download the latest executable in the [releases](https://github.com/pixelatedjelly/WeightCalcTool/releases/) section.
# Installation
Clone the repo by executing the following command:
```
git clone https://github.com/pixelatedjelly/WeightCalcTool.git
```
# Usage
1. Run the code by executing the command below, or run the executable.<br>
```
python WeightCalcTool.py
```
2. The main window GUI will appear.<br>
![Main window](https://i.imgur.com/xkcbhcs.png)<br>
3. Input your weight.<br>
4. Select your preferred unit of weight (yes, technically they're units of mass).<br>
5. Hit **Start**.<br>
6. A infobox will display the result.<br>
![Result infobox](https://i.imgur.com/Dzo6oX7.png)
# Packaging into a EXE
PyInstaller may be used to package the Python script into an executable file:
```
pyinstaller --onefile --noconsole --icon=icon.ico --version-file version WeightCalcTool.py
```
# Contributing
Contributions are welcome.
1. Fork the project
2. Create your feature branch (`git checkout -b feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature`)
5. Open a pull request
