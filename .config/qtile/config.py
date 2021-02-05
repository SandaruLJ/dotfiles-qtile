# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


### Imports
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import (Click, Drag, Group, Key, Screen, Match,
    ScratchPad, DropDown)
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess


### Custom variables
mod = "mod4"
terminal = guess_terminal()


### Keys
keys = [
    # Switch between windows in current stack pane
    Key([mod], "Down", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "Up", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([mod], "Left", lazy.layout.left(), 
        desc="Move focus down in stack pane"),
    Key([mod], "Right", lazy.layout.right(),
        desc="Move focus up in stack pane"),

    Key([mod], "j", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "k", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([mod], "h", lazy.layout.left(),
        desc="Move focus down in stack pane"),
    Key([mod], "l", lazy.layout.right(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down in current stack"),
    Key([mod, "control"], "Up", lazy.layout.shuffle_up(),
        desc="Move window up in current stack"),
    Key([mod, "control"], "Left", lazy.layout.shuffle_left(),
        desc="Move window down in current stack"),
    Key([mod, "control"], "Right", lazy.layout.shuffle_right(),
        desc="Move window up in current stack"),

    Key([mod, "control"], "j", lazy.layout.shuffle_down(),
        desc="Move window down in current stack"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(),
        desc="Move window up in current stack"),
    Key([mod, "control"], "h", lazy.layout.shuffle_left(),
        desc="Move window down in current stack"),
    Key([mod, "control"], "l", lazy.layout.shuffle_right(),
        desc="Move window up in current stack"),

    # Resize windows (Column layout)
    Key([mod, "shift"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "shift"], "Up", lazy.layout.grow_up(),
        desc="Grow window up"),
    Key([mod, "shift"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),

    Key([mod, "shift"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "shift"], "k", lazy.layout.grow_up(),
        desc="Grow window up"),
    Key([mod, "shift"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "shift"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),

    # Resize windows (MonadTall layout)
    Key([mod], "period", lazy.layout.grow(),
        desc="Grow window in MonadTall"),
    Key([mod], "comma", lazy.layout.shrink(),
        desc="Shrink window in MonadTall"),
    Key([mod, "shift"], "period", lazy.layout.grow_main(),
        desc="Grow master window in MonadTall"),
    Key([mod, "shift"], "comma", lazy.layout.shrink_main(),
        desc="Shrink master window in MonadTall"),
    Key([mod], "m", lazy.layout.maximize(), 
        desc="Maximize window in MonadTall"),
    Key([mod], "n", lazy.layout.normalize(), 
        desc="Reset secondary windows to default sizes"),
    Key([mod, "shift"], "n", lazy.layout.reset(), 
        desc="Reset all windows to their default sizes"),

    # Flip layout (MonadTall layout)
    Key([mod, "control"], "space", lazy.layout.flip(),
        desc="Flip the MonadTall layout"),

    # Toggle floating window
    Key([mod, "control"], "f", lazy.window.toggle_floating(),
        desc="Toggle floating window"),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "control"], "s", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Toggle fullscreen
    Key([], "F11", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen"),
    
    # Open application launcher
    Key([mod], "e", lazy.spawn("rofi -show drun"),
        desc="Open application launcher"),
    Key([mod], "w", lazy.spawn("rofi -show window"),
        desc="Open window selector"),

    # Launch terminal in current working directory
    Key([mod, "shift"], "Return",
        lazy.spawn("sh -c 'alacritty --working-directory \"$(xcwd)\"'"),
        desc="Launch terminal in current working directory"),
    
    # Launch file manager
    Key([mod], "backslash", lazy.spawn("thunar"), desc="Launch thunar"),
    Key([mod, "shift"], "backslash", lazy.spawn("sh -c 'thunar \"$(xcwd)\"'"),
        desc="Launch file manager in current working directory"),

    # Volume control
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key(["shift"], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 2")),
    Key(["shift"], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 2")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),

    # Lock screen
    Key(["mod1", "control"], "l", lazy.spawn(
        os.path.expanduser("~/.config/qtile/lock_screen.sh")), 
        desc="Lock screen"),

    # Change wallpaper
    Key([mod, "control"], "w", lazy.spawn(
        os.path.expanduser("~/.config/qtile/wallpaper_cycle.sh --next")),
        desc="Change to next wallpaper"),
    Key([mod, "control", "shift"], "w", lazy.spawn(
        os.path.expanduser("~/.config/qtile/wallpaper_cycle.sh --prev")),
        desc="Change to previous wallpaper"),
]


### Workspaces
groups = [
    Group(name="a", label="", layout="monadtall",
        matches=[
            Match(wm_class="Alacritty"),
        ]),
    Group(name="s", label="", layout="monadtall",
        matches=[
            Match(wm_class="Thunar"),
        ]),
    Group(name="d", label="", layout="max",
        matches=[
            Match(wm_class="firefox"),
        ]),
    Group(name="f", label="", layout="max",
        matches=[
            None,
        ]),
    Group(name="u", label="", layout="monadtall",
        matches=[
            None, 
        ]),
    Group(name="i", label="", layout="monadtall",
        matches=[
            None,
        ]),
    Group(name="o", label="", layout="max",
        matches=[
            None,
        ]),
    Group(name="p", label="", layout="monadtall",
        matches=[
            Match(wm_class="Lxappearance"),
        ]),
]

for group in groups:
    keys.extend([
        # Switch to workspace
        Key([mod], group.name, lazy.group[group.name].toscreen(),
            desc="Switch to workspace '{}'".format(group.name)),
        # Switch to and move focused window to workspace
        Key([mod, "shift"], group.name,
            lazy.window.togroup(group.name, switch_group=True),
            desc="Move window to workspace {}".format(group.name)),
    ])


### Dropdown windows
groups.append(
    ScratchPad("scratchpad", [
        DropDown("dd_term", terminal, opacity=0.8),
        DropDown("dd_fm", "thunar"),
    ]),
)

keys.extend([
    Key([mod, "shift", "control"], "Return",
        lazy.group["scratchpad"].dropdown_toggle("dd_term"),
        desc="Open terminal as a dropdown window"),
    Key([mod, "shift", "control"], "backslash",
        lazy.group["scratchpad"].dropdown_toggle("dd_fm"),
        desc="Open file manager as a dropdown window"),
])


### Colors
colors = dict(
        bg="#181818",
        accent="8AB4F8",
    )


### Layouts
layout_config = dict(
        border_width=2,
        border_focus=colors['accent'],
    )

layouts = [
    layout.Max(**layout_config),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(margin=4, insert_position=1),
    # layout.Matrix(),
    layout.MonadTall(margin=8, **layout_config),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(**layout_config),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=8,
)
extension_defaults = widget_defaults.copy()


### Bottom Bar
screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    font="Font Awesome",
                    fontsize=16,
                    disable_drag=True,
                    highlight_method="line",
                    highlight_color="#000000",
                    this_current_screen_border=colors['accent'],
                    this_screen_border=colors['accent'],
                    padding=3,
                ),
                widget.Prompt(
                    prompt="  ",
                    font="monospace",
                    foreground="#76B041",
                    cursor_color="#FFFFFF",
                    background="#000000",
                    padding=4,
                ),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
                    text="",
                    fontsize=16,
                    mouse_callbacks={
                        'Button1': lambda qtile: qtile.cmd_spawn(
                            os.path.expanduser(
                                "~/.config/qtile/wallpaper_cycle.sh --next")
                        ),
                        'Button3': lambda qtile: qtile.cmd_spawn(
                            os.path.expanduser(
                                "~/.config/qtile/wallpaper_cycle.sh --prev")
                        ),
                    }
                ),
                widget.Net(format="{down} ↓ {up} ↑", background="#2191FB"),
                widget.Cmus(background="#76B041"),
                widget.Systray(),
                widget.Volume(background="#C33C54"),
                widget.Clock(format='%a %d %b %H:%M', background="#76B041"),
                widget.CurrentLayoutIcon(scale=0.75),
            ],
            24, background=colors['bg'],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
], **layout_config)
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# Auto start applications
@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call(script)

