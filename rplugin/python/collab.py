import neovim

@neovim.plugin
class Collaborate(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.command('CollabStart', range='', nargs='*', sync=False)
    def start_collab(self, args, range):
        vim.command('echo "Started Collaboration"')
