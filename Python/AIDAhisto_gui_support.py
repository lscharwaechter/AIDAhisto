""""
GUI module generated by PAGE version 4.22
in conjunction with Tcl version 8.6
May 02, 2019 01:11:59 PM CEST  platform: Darwin

@authors: Niklas Pallast
Department of Neurology, University Hospital Cologne

AIDAhisto: Atlas-based imaging data analysis tool for mouse brain histology
"""

import sys,os

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
    import tkinter.filedialog as fileDia
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.filedialog as fileDia
    py3 = True

def set_Tk_var():
    global inputFilename
    inputFilename = tk.StringVar()
    global fast
    fast = tk.StringVar()
    global dark
    dark = tk.StringVar()
    global bar
    bar = tk.StringVar()
    global red_v
    red_v = tk.StringVar()
    global green_v
    green_v = tk.StringVar()
    global blue_v
    blue_v = tk.StringVar()
    global cell_widthV
    cell_widthV = tk.DoubleVar()
    cell_widthV.set(10.0)
    global cell_width_entry
    cell_width_entry = tk.StringVar()
    cell_width_entry.set(round(cell_widthV.get(),2))
    global min_dist
    min_dist = tk.DoubleVar()
    min_dist.set(round(cell_widthV.get()/2,2))
    global cell_dist_entry
    cell_dist_entry = tk.StringVar()
    cell_dist_entry.set(round(min_dist.get(),2))
    global roi_inV
    roi_inV = tk.StringVar()
    roi_inV.set("Image with associated ROIs...")
    global ref_inV
    ref_inV = tk.StringVar()
    ref_inV.set("Image with reference positions...")
    global listofRoiNames
    listofRoiNames = tk.StringVar()
    listofRoiNames.set("txt.file with ROI Names...")
    global threshold
    threshold = tk.DoubleVar()
    threshold.set(10.0)
    global threshold_entry
    threshold_entry = tk.StringVar()
    threshold_entry.set(round(threshold.get(),2))

def apply_cmd():
    if os.path.exists(inputFilename.get()):
        fn = inputFilename.get()
    else:
        print('Choose a valid input file...')
        return

    roiV = ''
    if os.path.exists(roi_inV.get()):
        roiV = ' -a ' + roi_inV.get()+' '

    refV = ''
    if os.path.exists(ref_inV.get()):
        refV = ' -r ' + ref_inV.get()+' '

    listV = ''
    if os.path.exists(listofRoiNames.get()):
        listV = ' -l '+listofRoiNames.get()+' '

    options=''
    if fast.get():
        options = options+' -f '
    if dark.get():
        options = options + ' -d '
    if bar.get():
        options = options + ' -b '

    colorStr=' -c '
    if red_v.get():
        colorStr=colorStr+'0 '
    elif green_v.get():
        colorStr=colorStr+'1 '
    elif blue_v.get():
        colorStr=colorStr+'2 '
    else:
        print('Choose a color channel...')
        return

    command = 'python AIDAhisto.py '+fn+colorStr+'-w '+cell_width_entry.get()+' -m '+cell_dist_entry.get()+options+' -t '+threshold_entry.get()+refV+roiV+listV


    print(command)
    os.system(command)
    sys.stdout.flush()
def bar_cmd():
    print('-b')
    sys.stdout.flush()

def blue_cmd():
    green_v.set('')
    red_v.set('')

def dark_cmd():
    print('-d')
    sys.stdout.flush()

def dist_cmd(*args):
    cell_dist_entry.set(round(min_dist.get(),2))

def fast_cmd():
    print('-f ')
    sys.stdout.flush()

def green_cmd():
    blue_v.set('')
    red_v.set('')

def list_cmd():
    filename = fileDia.askopenfilename(title="Select txt. file with ROI names")
    listofRoiNames.set(filename)

def openfile_cmd():
    filename = fileDia.askopenfilename(title="Select image data")
    inputFilename.set(filename)

def red_cmd():
    green_v.set('')
    blue_v.set('')

def ref_cmd():
    filename = fileDia.askopenfilename(title="Select image with reference cell positions")
    ref_inV.set(filename)

def roi_cmd():
    filename = fileDia.askopenfilename(title="Select image with associted ROIs")
    roi_inV.set(filename)

def threshold_cmd(*args):
    threshold_entry.set(round(threshold.get(),2))

def width_cmd(*args):
    cell_width_entry.set(round(cell_widthV.get(),2))
    min_dist.set(round(cell_widthV.get()/2,2))
    dist_cmd()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import AIDAhisto_gui
    AIDAhisto_gui.vp_start_gui()




