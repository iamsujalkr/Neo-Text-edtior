import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

# Create the main window
main_app = tk.Tk()
def set_window_size(main_app, width_ratio=0.85, height_ratio=0.85):
    """Sets the main window size based on screen dimensions"""
    # Get screen width and height
    screen_width = main_app.winfo_screenwidth()
    screen_height = main_app.winfo_screenheight()

    # Calculate window width and height
    window_width = int(screen_width * width_ratio)
    window_height = int(screen_height * height_ratio)

    # Center the window
    x = (screen_width/2) - (window_width/2)
    y = (screen_height/2) - (window_height/2 + 28)

    main_app.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
set_window_size(main_app)
main_app.title('Neo text editor')
main_app.wm_iconbitmap('icon.ico')

################################ main menu ################################
main_menu = tk.Menu()

##### File menu
file = tk.Menu(main_menu, tearoff=False)
# file icons
new_icon = tk.PhotoImage(file='icons/new.png')
open_icon = tk.PhotoImage(file='icons/open.png')
save_icon = tk.PhotoImage(file='icons/save.png')
save_as_icon = tk.PhotoImage(file='icons/save_as.png')
exit_icon = tk.PhotoImage(file='icons/exit.png')

##### Edit menu
edit = tk.Menu(main_menu, tearoff=False)
# edit icons
copy_icon = tk.PhotoImage(file='icons/copy.png')
paste_icon = tk.PhotoImage(file='icons/paste.png')
cut_icon = tk.PhotoImage(file='icons/cut.png')
clear_all_icon = tk.PhotoImage(file='icons/clear_all.png')
find_icon = tk.PhotoImage(file='icons/find.png')

##### View menu
view = tk.Menu(main_menu, tearoff=False)
# view icons
tool_bar_icon = tk.PhotoImage(file='icons/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons/status_bar.png')

##### Color theme menu
color_theme = tk.Menu(main_menu, tearoff=False)
# color icons
light_defautlt_icon = tk.PhotoImage(file='icons/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons/light_plus.png')
dark_icon = tk.PhotoImage(file='icons/dark.png')
red_icon = tk.PhotoImage(file='icons/red.png')
monokai_icon = tk.PhotoImage(file='icons/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons/night_blue.png')
custom_icon = tk.PhotoImage(file='icons/custom.png')

color_icon = (light_defautlt_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon, custom_icon)
color_dict = {
    'Light Default' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' : ('#ededed', '#6b9dc2'),
    'Custom' : ""
}

main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)
# ----------------------------- End main menu -----------------------------


################################ tool bar ################################
tool_bar = ttk.Label(main_app)
tool_bar.pack(side=tk.TOP, fill=tk.X)

# font box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)

# size box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable=size_var, state='readonly')
font_size['values'] = tuple(range(8, 81, 2))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

# bold button
bold_icon = tk.PhotoImage(file='icons/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

# italic button
italic_icon = tk.PhotoImage(file='icons/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

# underline button
underline_icon = tk.PhotoImage(file='icons/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

# font color button
font_color_icon = tk.PhotoImage(file='icons/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=5)

# align left
align_left_icon = tk.PhotoImage(file='icons/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

# align center
align_center_icon = tk.PhotoImage(file='icons/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

# align right
align_right_icon = tk.PhotoImage(file='icons/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)
# ----------------------------- End tool bar -----------------------------


################################ text editor ################################
text_editor = tk.Text(main_app)
text_editor.config(wrap='word', relief=tk.FLAT)
scroll_bar = tk.Scrollbar(main_app)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
text_editor.configure(font=('Arial', 16))

### font functionality
current_font_family = 'Arial'
current_font_size = 12
bold = 'normal'
italic = 'roman'
underline = 0

def change_font(event=None):
    """Sets the font of text editior as the user wants"""
    global current_font_family
    global current_font_size
    global bold
    global italic
    global underline
    current_font_family = font_family.get()
    current_font_size = size_var.get()
    text_property = font.Font(family=current_font_family, size=current_font_size, weight=bold, slant=italic, underline=underline)
    text_editor.configure(font=text_property)
    text_editor.focus_set()

# bold button functionality
def change_bold(e=None):
    """Sets the bold feature on/off"""
    global bold
    bold = 'bold' if bold == 'normal' else 'normal'
    change_font()

# italic button functionality
def change_italic(e=None):
    """Sets the italic feature on/off"""
    global italic
    italic = 'italic' if italic == 'roman' else 'roman'
    change_font()

# underline button functionality
def change_underline(e=None):
    """Sets the underline feature on/off"""
    global underline
    underline = 1 if underline == 0 else 0
    change_font()

# font color functionality
def change_font_color():
    """Change the font color as the user wants"""
    color_var = colorchooser.askcolor(title="Select the text color")
    text_editor.configure(fg=color_var[1])
    text_editor.focus_set()

### align functionality
def align_left():
    """Makes the text alignment to left"""
    text_content = text_editor.get(1.0, 'end-1c')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')
    text_editor.focus_set()

def align_center():
    """Makes the text alignment to center"""
    text_content = text_editor.get(1.0, 'end-1c')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')
    text_editor.focus_set()

def align_right():
    """Makes the text alignment to right"""
    text_content = text_editor.get(1.0, 'end-1c')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')
    text_editor.focus_set()


# button commands
font_box.bind('<<ComboboxSelected>>', change_font)
font_size.bind('<<ComboboxSelected>>', change_font)
bold_btn.configure(command=change_bold)
italic_btn.configure(command=change_italic)
underline_btn.configure(command=change_underline)
font_color_btn.configure(command=change_font_color)
align_left_btn.configure(command=align_left)
align_center_btn.configure(command=align_center)
align_right_btn.configure(command=align_right)
# ----------------------------- End text editor -----------------------------


################################ status bar ################################
status_bar = ttk.Label(main_app, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def changed(event=None):
    """Updates the status bar with any modifications in text editor"""
    global text_changed
    if (text_editor.edit_modified()):
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} | Words : {words}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>', changed)
# ----------------------------- End status bar -----------------------------


################################ main menu functionality ################################
url = ''
def new_file(event=None):
    """Opens a new file for working"""
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if (mbox is True):
                save_file()
    except:
        return
    url = ''
    text_editor.delete(1.0, tk.END)
    text_changed = False

def open_file(event=None):
    """Opens an existing file for working"""
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_app.title(os.path.basename(url))

def save_file(event=None):
    """Saves the current working file"""
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
            content = str(text_editor.get(1.0, tk.END))
            url.write(content)
            url.close()
    except:
        return

def save_as_file():
    """Saves the current working as new file"""
    global url
    try:
        content = str(text_editor.get(1.0, tk.END))
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
        url.write(content)
        url.close()
    except:
        return

def exit_func(event=None):
    """Ask for saving the file before exiting"""
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if (mbox is True):
                save_file()
                main_app.destroy()
            elif (mbox is False):
                main_app.destroy()
        else:
            main_app.destroy()
    except:
        return
    
# File commands
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)
file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)
file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S', command=save_file)
file.add_command(label='Save as', image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=save_as_file)
file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_func)

# edit commands
def find_func(event=None):
    """Find or Replace any character"""
    def find():
        """finds the given characters in the text editor"""
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        match = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                match += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    def replace():
        """Replace the given characters in the tex editor"""
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    def find_close():
        """Removes the tag before closing Find/Replace dialog box"""
        text_editor.tag_remove('match', '1.0', tk.END)
        find_dialogue.destroy()

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+800+150')
    find_dialogue.title('Find/Replace')
    find_dialogue.resizable(0,0)
    find_dialogue.wm_iconbitmap('icon.ico')
    find_dialogue.protocol('WM_DELETE_WINDOW',find_close)

    # frame
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=35)

    # label
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text='Replace : ')

    # entry box
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    # button frame
    btn_frame = ttk.Frame(find_frame)

    # button
    find_btn = ttk.Button(btn_frame, text='Find', command=find)
    replace_btn = ttk.Button(btn_frame, text='Replace', command=replace)

    # label grid 
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    # entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    # button grid
    btn_frame.grid(row=2, columnspan=2)
    find_btn.grid(row=0, column=0, padx=8, pady=4)
    replace_btn.grid(row=0, column=1, padx=8, pady=4)

edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C', command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+V', command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X', command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All', image=clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+R', command=lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F', command=find_func)

# view checkbuttons
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    """Hides/Show the toolbar"""
    global show_toolbar
    if (show_toolbar):
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    """Hides/Show the status bar"""
    global show_statusbar
    if (show_statusbar):
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True

view.add_checkbutton(label='Tool Bar', onvalue=True, offvalue=False, variable=show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar', onvalue=True, offvalue=False, variable=show_statusbar, image=status_bar_icon, compound=tk.LEFT, command=hide_statusbar)

# color theme radio buttons
theme_choice = tk.StringVar()
def change_theme(event=None):
    """Changes the theme of text editor"""
    chosen_theme = theme_choice.get()
    if (chosen_theme == 'Custom'):
        fg = colorchooser.askcolor(title="Select the text color")
        bg = colorchooser.askcolor(title="Select the background color")
        fg_color = fg[1]
        bg_color = bg[1]
    else:
        color_tuple = color_dict.get(chosen_theme)
        fg_color, bg_color = color_tuple
    text_editor.config(background=bg_color, foreground=fg_color)

count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icon[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count+=1
# ----------------------------- End main menu functionality -----------------------------


main_app.config(menu=main_menu)
main_app.bind("<Control-n>", new_file)
main_app.bind("<Control-o>", open_file)
main_app.bind("<Control-s>", save_file)
main_app.bind("<Control-Alt-s>", save_as_file)
main_app.bind("<Control-q>", exit_func)
main_app.bind("<Control-f>", find_func)
main_app.bind("<Control-b>", change_bold)
main_app.bind("<Control-i>", change_italic)
main_app.bind("<Control-u>", change_underline)
main_app.protocol('WM_DELETE_WINDOW', exit_func)
main_app.mainloop()