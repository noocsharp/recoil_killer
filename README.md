Recoil Killer
=============

This is a utility for canceling recoil in Counter-Strike: Global Offensive (CS:GO). The user can use the editor to input vectors
for mouse movement that will then be converted into standalone python scripts that will cancel the recoil. It includes time intervals
that can be changed as the guns in CS have different rates of fire, and also a way to input in-game sensitivity, assuming the player has
raw_input 1 in-game.

The recoil killer client detects which gun selection button has been pressed most recently, and uses this to determine which script to run. 
As a result, the user has to tell the client which script needs to be run corresponding to their primary weapon.

While this is what this utility has been designed for, it can also be used for other things. If you modify the code a little bit, you
can probably make the program run any python script with a key press, although personally I do not recommend it because there are much 
better programs to do this.

Important Info
--------------

At the moment, the script editor and scripts work, *but the client does not*. The client is simply a way to run the script in the right circumstance (when the primary weapon is selected and left mouse button is being held down), and I'm sure there are other ways to get the scripts to run in these circumstances.

There is a script for the M4A1-S included as an example. It doesn't work very well but it demonstrates how the editor structures the scripts. If you make a script and feel particularly proud of it, feel free to send a pull request to make it more easily available for others to use.

Dependencies
------------

The script editor requires pywin32. The editor itself was written in Python 3.6 and uses the 32-bit version of both pywin32 and Python 3.6.

The client (which at the moment is dysfunctional) relies on pyHook.

How to use the script editor
----------------------------

First of all, you need to install pywin32 for whichever version of Python 3 that you are using. Then, clone this repository and run "recoil_killer_editor.py".

To start writing a script, simply click the add button to add a vector. This vector will move the mouse cursor relative to the crosshair which CS:GO automatically resets to the center when the game finds out about the event. You should set the sensitivity to your in-game sensitivity assuming you use "raw_input 1". You should also set the time interval based on the RPM of the gun that you're trying to make a script for. You can calculate the time interval according to the following equation:

time interval = 1/(RPM/60)

After you have created a filler script (or an actual script if you want), you can save it using the write button. Input the name of the file, which will be a python script, and it will be saved to the scripts directory. In addition, if you want to test your script, you can open CS:GO onto a bot map and press the "Write + Test" button in the program. This will run the script, and should cancel recoil somewhat if your script is accurate. The program includes this button to make testing more streamline, so you don't have to press "Write" and then "Test" buttons every time you want to test your script.