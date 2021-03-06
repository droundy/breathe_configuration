from dragonfly import Dictation, AppContext, Text, Key, IntegerRef
from breathe import Breathe, CommandContext

context = CommandContext("firefox")

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    # context = AppContext(title=".py") | CommandContext("python"),
    context = context,
    mapping = {
        'page back': Key('a-left'),
        'page forward': Key('a-right'),
        'page reload': Key('c-r'),

        '[<n>] link next': Key('tab:%(n)d'),
        '[<n>] link previous': Key('s-tab:%(n)d'),
        'link follow': Key('enter'),

        '[<n>] tab right': Key('c-pgdown:%(n)d'),
        '[<n>] tab left': Key('c-pgup:%(n)d'),
        'tab new': Key('c-t'),
    },
    extras = [
        IntegerRef("n", 1, 20, default=1),
        Dictation("text", default=""),
    ]
)
