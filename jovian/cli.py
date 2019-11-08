import sys

import click

from jovian._version import __version__
from jovian.utils.clone import clone, pull
from jovian.utils.configure import configure, reset
from jovian.utils.extension import setup_extension
from jovian.utils.install import activate, install
from jovian.utils.slack import add_slack


@click.group()
@click.version_option(version=__version__, prog_name="Jovian")
@click.pass_context
def main(ctx, log_level="info"):
    """Keep track of your Jupyter notebooks using Jovian.

    Use within your Jupyter notebooks:

        [1] import jovian

        [2] jovian.commit()

    Or try out a demo with:

        $ jovian clone aakashns/jovian-tutorial
    """

    pass


@main.command("help")
@click.pass_context
def help(ctx):
    """Print this help message."""

    # Pretend user typed 'jovian --help' instead of 'jovian help'.
    sys.argv[1] = "--help"
    main()


@main.command('version')
@click.pass_context
def main_version(ctx):
    """Print Jovian’s version number."""

    # Pretend user typed 'jovian --version' instead of 'jovian version'
    sys.argv[1] = "--version"
    main()


@main.command("configure")
@click.pass_context
def create_config(ctx):
    """Configure Jovian for Pro users."""

    configure()


@main.command("reset")
@click.pass_context
def reset_config(ctx):
    """Reset Jovian config."""

    reset()


@main.command("install", short_help="Install packages from environment file.")
@click.argument('name_argv', nargs=-1)
@click.pass_context
def install_env(ctx, name_argv):
    """Install packages from environment file:

        $ jovian install

    or, install from specific environment file

        $ jovian install environment-linux.yml
    """

    num_args = len(name_argv)

    if num_args == 0:
        install()
    elif num_args == 1:
        install(env_name=name_argv[0])
    else:
        # Show help
        sys.argv[1] = "--help"
        install_env()


@main.command("activate")
@click.pass_context
def activate_env(ctx, name_argv):
    """Activate conda environment from environment file."""

    activate()


@main.command("clone", short_help="Clone a notebook hosted on Jovian")
@click.argument('notebook')
@click.option('-v', '--version', 'version')
@click.pass_context
def exec_clone(ctx, notebook, version):
    """Clone a notebook hosted on Jovian:

        $ jovian clone aakashns/jovian-tutorial

    Or clone a specific version of notebook:

        $ jovian clone aakashns/jovian-tutorial -v 10
    """

    clone(notebook, version)


@main.command("pull", short_help="Fetch new version of notebook hosted Jovian.")
@click.argument('notebook')
@click.option('-v', '--version', 'version')
@click.pass_context
def exec_pull(ctx, notebook, version):
    """Fetch new version of notebook hosted on Jovian(into current directory):

        $ jovian pull aakashns/jovian-tutorial

    Or fetch a specific version of notebook:

        $ jovian pull aakashns/jovian-tutorial -v 10
    """

    pull(notebook, version)


@main.command("add-slack")
@click.pass_context
def exec_add_slack(ctx):
    """Connect slack to get updates."""

    add_slack()


@main.command("enable-extension")
@click.pass_context
def extension_enable(ctx):
    """Enable Jovian’s Jupyter notebook extension."""

    setup_extension(enable=True)


@main.command("disable-extension")
@click.pass_context
def extension_disable(ctx):
    """Disable Jovian’s Jupyter notebook extension."""

    setup_extension(enable=False)


if __name__ == '__main__':
    main()
