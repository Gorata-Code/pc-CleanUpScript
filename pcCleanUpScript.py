# This Python file uses the following encoding: utf-8
import os
import sys
import pyautogui as pyag

pyag.FAILSAFE = True


def wait(duration: float = 1) -> None:

    # Customising pyautogui.sleep() to make it flexible and easier to work with.

    time_unit: str

    if duration > 1:
        time_unit = 'seconds'
    else:
        time_unit = 'second'

    print(f'\n\tWait:{duration} {time_unit}.\n')
    pyag.sleep(duration)


def maximise_window() -> None:
    wait()
    pyag.hotkey('winleft', 'up')
    wait()


def search(process_name: str) -> None:

    # Searching the Run dialog.

    pyag.hotkey('winleft', 'r')
    wait()
    pyag.typewrite(process_name, 0.3)
    pyag.press('Enter')
    wait(2)

    # Dealing with the Temporary Folder
    if process_name == '%temp%':
        while not pyag.locateCenterOnScreen(f"{resource_path('')}tempWindow.png"):
            print('\n\tWaiting for the Temp window to open up...')
            wait(3)
            print('\tIf the Temp window has opened up on another monitor, please drag it over to your main '
                  f'display.')
            wait()

        wait()

    else:
        # Dealing with the Prefetch Folder
        while not pyag.locateCenterOnScreen(f'{resource_path("")}prefetchWindow.png'):
            print(f'\n\tWaiting for the Prefetch window to open up...')
            print('\tIf the Prefetch window has opened up on another monitor, please drag it over to your main '
                  f'display.')
            wait(4)
            pyag.locateCenterOnScreen(f'{resource_path("")}youDontHaveAccessToThisFolder.png')
            print('Administrator Access')
            pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}prefetchContinue.png'), duration=2)
            pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}prefetchContinueLined.png'), duration=2)
            wait()
            pyag.click()
            wait()


def get_screenshot(screenshot_id: str) -> None:

    """

    Getting a screenshot of the number of files and the amount of space they use. This is just so I can track the
    amount of freed up space.

    """

    maximise_window()

    print('\nChecking the folder Properties...')

    pyag.hotkey('ctrl', 'a')
    wait()
    pyag.moveTo(x=629, y=64, duration=2)  # Click on Properties (Alt+Enter)
    wait()
    pyag.click()
    wait(2)
    pyag.screenshot(screenshot_id)  # Take a Screenshot of the 'Properties' pane
    wait()


def recycling() -> None:

    # I use this functionality quite a lot, so I figured it would be best to give it its own function.

    while pyag.locateCenterOnScreen(f'{resource_path("")}recycling.png'):
        print('Recycling...')
        wait(3)


def delete() -> None:

    # The actual deleting of the files from the Temporary files folder and the Prefetch folder.

    wait()
    pyag.press('esc')
    wait()
    pyag.press('delete')
    wait(3)

    recycling()

    if pyag.locateCenterOnScreen(f'{resource_path("")}doThisForAllCurrentItems.png') or pyag.locateCenterOnScreen(
            f'{resource_path("")}doThisForAllCurrentItemsUnderlined.png'):
        pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}doThisForAllCurrentItems.png'), duration=2)
        pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}doThisForAllCurrentItemsUnderlined.png'),
                    duration=1)
        pyag.click()

    if pyag.locateCenterOnScreen(f'{resource_path("")}skip.png') or pyag.locateCenterOnScreen(
            f'{resource_path("")}skipUnderlined.png'):
        pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}skip.png'), duration=1)
        pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}skipUnderlined.png'), duration=1)
        pyag.click()
        wait(2)

    recycling()

    if pyag.locateCenterOnScreen(f'{resource_path("")}continue.png') or pyag.locateCenterOnScreen(
            f'{resource_path("")}continueUnderlined.png'):
        print('Clicking Continue...')
        pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}continue.png'), duration=1)
        pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}continueUnderlined.png'), duration=1)
        pyag.click()
        wait(2)

    recycling()

    while pyag.locateCenterOnScreen(f'{resource_path("")}fileInUse.png'):
        pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}doThisForAllCurrentItems.png'), duration=1)
        pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}doThisForAllCurrentItemsUnderlined.png'), duration=1)
        pyag.click()
        wait()

        if pyag.locateCenterOnScreen(f'{resource_path("")}closeTheFileAndTryAgain.png'):
            pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}cancel.png'), duration=1)
            pyag.click()
            wait()
            pyag.click()
            wait()

        else:
            pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}prefetchContinue.png'), duration=1)
            pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}prefetchContinueLined.png'), duration=1)
            pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}continue.png'), duration=1)
            wait()
            pyag.click()
            wait()

    recycling()

    pyag.hotkey('alt', 'f4')


def still_cleaning_up() -> None:

    while pyag.locateCenterOnScreen(f'{resource_path("")}cleaningUp.png'):
        print('Still cleaning up...')
        if pyag.locateCenterOnScreen(f'{resource_path("")}continue.png'):
            pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}continue.png'), duration=1)
            wait()


def disk_cleanup() -> None:

    # Handling the 'Disk Clean Up' routine.

    pyag.press('winleft')
    wait()
    pyag.typewrite('Disk Clean', 0.2)
    wait()
    pyag.press('enter')
    wait(2)

    while not pyag.locateCenterOnScreen(f'{resource_path("")}diskCleanUpDriveSelection.png'):
        print('Drive Selection Loading...')
        wait(2)

    pyag.press('enter')

    wait(2)

    while not pyag.locateCenterOnScreen(f'{resource_path("")}diskCleanUpFor.png'):
        print('Disk Clean up is Calculating...')
        wait(2)

    while pyag.locateCenterOnScreen(f'{resource_path("")}uncheckedBox.png'):
        pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}uncheckedBox.png'))
        pyag.click()
        wait()

    pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}downwardScrollArrow.png'), duration=1)
    pyag.click(clicks=2, interval=1)

    while pyag.locateCenterOnScreen(f'{resource_path("")}uncheckedBox.png'):
        pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}uncheckedBox.png'), duration=1)
        pyag.click()
        wait()

    pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}okay.png'), duration=1)
    pyag.click()
    pyag.press('enter')  # Confirm delete
    wait(3)

    still_cleaning_up()

    wait(2)

    if pyag.locateCenterOnScreen(f'{resource_path("")}fileAccessDenied.png'):
        pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}recycleBinContinue.png'), duration=1)
        pyag.click()
        wait()

    still_cleaning_up()

    wait(2)

    print('Automated Disk Clean up Completed Successfully!')


def recycle_bin() -> bool:

    status: bool

    print('\nNow off to clean your Recycle Bin...')

    wait()

    pyag.press('winleft')
    wait()
    pyag.typewrite('File Explorer', 0.2)
    wait()
    pyag.press('Enter')
    wait(2)
    while not pyag.locateCenterOnScreen(f'{resource_path("")}thisPCWindow.png'):
        print('Loading File Explorer...')
        wait(2)

    maximise_window()

    pyag.press('Tab', presses=3, interval=1)
    pyag.press('Enter')
    pyag.typewrite('Recycle Bin', 0.2)
    pyag.press('Enter')
    wait()
    while not pyag.locateCenterOnScreen(f'{resource_path("")}recycleBinWindow.png'):
        print('Opening up your Recycle Bin...')
        wait()

    wait()
    if pyag.locateCenterOnScreen(f'{resource_path("")}zeroItems.png'):
        print('Your Recycle bin is already empty!')
        status: bool = False
        return status

    if not pyag.locateCenterOnScreen(f'{resource_path("")}zeroItems.png'):
        pyag.screenshot('Recycle Bin before clearing.png')
        wait()

        pyag.moveTo(x=30, y=74, duration=1)  # Moving to 'Empty Recycle Bin' icon.
        pyag.click()
        wait()
        pyag.press('Enter')
        wait(2)

        while pyag.locateCenterOnScreen(f'{resource_path("")}deleting.png'):
            print('Clearing up your Recycle Bin...')
            wait(4)

        wait()
        if pyag.locateCenterOnScreen(f'{resource_path("")}fileAccessDenied.png'):
            pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}recycleBinContinue.png'), duration=1)
            pyag.click()
            wait()

        while pyag.locateCenterOnScreen(f'{resource_path("")}workingOnIt.png'):
            print('Still clearing up your Recycle Bin...')
            wait(4)

            x: int = int(pyag.size()[0] / 2)  # Half the screen width
            y: int = int(pyag.size()[1] / 2)  # Half the screen height

            pyag.moveTo(x=x - 25, y=y, duration=1)  # Screen centre
            pyag.click()
            wait()
            pyag.rightClick()
            wait()

            while not pyag.locateCenterOnScreen(f'{resource_path("")}refresh.png'):
                print('Refreshing...')
                wait()

            pyag.moveTo(pyag.locateCenterOnScreen(f'{resource_path("")}refresh.png'), duration=1)
            pyag.click()
            wait()

        status: bool = True
        return status


def wrap_up(process_name) -> None:
    wait()
    print(f'\'{process_name.title()}\' completed!')


def recycle_bin_status() -> None:

    status = recycle_bin

    if status == True:

        ''' The line above only works in this form. If I write 'If status:...' it assumes I mean 'if status 
        is not null / None'. So it runs the code below regardless of whether status is 'True' or 'False'.
        '''
        print('Your Recycle Bin is all cleared up now! :) ')

    wait(2)

    pyag.hotkey('alt', 'f4')


def resource_path(relative_path) -> [bytes, str]:  # Managing our image assets, keeping them with our file.
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def main() -> None:

    print("""
               ***----------------------------------------------------------------------------------------***
         \t***------------------------ DUMELANG means GREETINGS! ~ G-CODE -----------------------***
                   \t***------------------------------------------------------------------------***\n
        \t"PC CLEANUP SCRIPT" Version 1.0.0\n
    This script will clean up your computer for temporary files and also clear your Recycle Bin to free up space. If 
    at any point you wish to stop it, simply move the mouse cursor to the top left corner of your screen and wait 
    until it terminates. Alternatively, you can close the command prompt window where this message is printed. 
    Cheers! """)

    processes: [{}] = [
        {'process_name': '%temp%', 'screenshot_id': f'{resource_path("")}Temporary Files.png'},
        {'process_name': 'prefetch', 'screenshot_id': f'{resource_path("")}Prefetch.png'}
    ]

    wait()

    for process in processes:
        search(process.get('process_name'))
        get_screenshot(process.get('screenshot_id'))
        delete()
        wrap_up(process.get('screenshot_id').split('\\')[-1][:-4])

    wait()

    disk_cleanup()

    recycle_bin()

    recycle_bin_status()

    input('Press Enter to quit: ')


if __name__ == '__main__':
    main()

