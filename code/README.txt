This is the instructions for using the crosswalk detection software. Has been verified on Linux (Ubuntu) and MacOS.

Installation

	1. Install Python 3 if it is not already installed (can be verified with the 		terminal command "python3 --version").

	2. When inside the directory of the project, run the following command in the 		terminal:

	pip3 install -r requirements.txt

	Or use pip3 to install numpy, librosa, scikit-learn independently.

Use

	1. After library installation and navigating to inside the "detection" directory, 	run the program by using the following in the terminal:

	python3 crosswalk_detection.py <COMMANDS>

	With <COMMANDS> arguments being:
	-c - If the audio files are in the current directory.
	-d <PATH> - If the audio files are in the directory at <PATH>. 
	NOTE - Make sure Python has the ability to read and write files at that <PATH>

	Example: 
	
	python3 crosswalk_detection.py -d ~/Documents/GitHub/ECE4271_Proj4/audio

	2. The terminal will print showing updates on progress periodically as all .wav 	files are analyzed.

 	The .txt results will be generated in either the current directory or at the 		<PATH> of the files as specified.

 	If .txt results already exist in that folder, the results will be appended to the 	end file. If not, a new file will be created.

NOTE - only crosswalk_detection.py is required. All Jupyter Notebooks (and accompanying conversion script notebook2script.py) are for visuals only.
