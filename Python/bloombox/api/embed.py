# -*- coding: utf-8 -*-

__doc__ = """

  bloombox: embed API client

"""

# std

# googs

# canteen
from canteen.util import cli

# local
from .. import auth
from .. import client
from .. import output


class Embed(cli.Tool):

  """ Tools for interacting with Embedded Menus. """

  ## config
  EMBED_SERVICE = "embed"
  EMBED_VERSION = "v1"

  embed_service = None


  class Data(cli.Tool):

    """ Tool for retrieving embedded menu data. """

    arguments = (
      ("partner", {"type": unicode, "help": "partner ID"}),
      ("location", {"type": unicode, "help": "location ID"}))

    def execute(arguments):

      """ Retrieve embedded menu data. """

      import pdb; pdb.set_trace()

      key = arguments.apikey or auth.API_KEY
      client_id = arguments.client or auth.CLIENT_ID
      client_secret = arguments.secret or auth.CLIENT_SECRET
      if not key:
        print "Must provide a valid API key via '--apikey'. For more info, run 'bloombox --help'."
        exit(1)
      if not client_id:
        print "Must provide a valid client ID via '--client'. For more info, run 'bloombox --help'."
        exit(1)
      if not client_secret:
        print "Must provide a valid client secret via '--secret'. For more info, run 'bloombox --help'."
        exit(1)

      auth.prepare_auth("Bloombox CLI", client_secret, client_id, key)
      Embed.embed_service = client.get_client(arguments, Embed.EMBED_SERVICE, Embed.EMBED_VERSION, authorized=True)
      menu_data = Embed.data(arguments.partner, arguments.location, arguments)
      output.object_output(menu_data)


  class View(cli.Tool):

    """ Tool for retrieving embedded menu view configuration. """

    arguments = (
      ("partner", {"type": unicode, "help": "partner ID"}),
      ("location", {"type": unicode, "help": "location ID"}),
      ("--style", "-s", {"type": unicode, "choices": {"MASTER_ONLY", "MASTER_DETAIL"}, "default": "MASTER_ONLY", "help": "display style"}))

    def execute(arguments):

      """ Retrieve embedded menu view metadata. """

      key = arguments.apikey or auth.API_KEY
      client_id = arguments.client or auth.CLIENT_ID
      client_secret = arguments.secret or auth.CLIENT_SECRET
      if not key:
        print "Must provide a valid API key via '--apikey'. For more info, run 'bloombox --help'."
        exit(1)
      if not client_id:
        print "Must provide a valid client ID via '--client'. For more info, run 'bloombox --help'."
        exit(1)
      if not client_secret:
        print "Must provide a valid client secret via '--secret'. For more info, run 'bloombox --help'."
        exit(1)

      auth.prepare_auth("Bloombox CLI", client_secret, client_id, key)
      Embed.embed_service = client.get_client(arguments, Embed.EMBED_SERVICE, Embed.EMBED_VERSION, authorized=True)
      view_data = Embed.view(arguments.partner, arguments.location, arguments.style, arguments)
      output.object_output(view_data)


  @staticmethod
  def data(partner, location, arguments=None):

    """ Formulate and execute an RPC to retrieve embedded menu data. """

    if Embed.embed_service is None:
      Embed.embed_service = client.get_client(arguments, Embed.EMBED_SERVICE, Embed.EMBED_VERSION, authorized=False)
    return output.execute(arguments, Embed.embed_service.data(partner=partner, location=location))

  @staticmethod
  def view(partner, location, style="MASTER_ONLY", arguments=None):

    """ Formulate and execute an RPC to fetch view info for an embedded menu. """

    if Embed.embed_service is None:
      Embed.embed_service = client.get_client(arguments, Embed.EMBED_SERVICE, Embed.EMBED_VERSION, authorized=False)
    return output.execute(arguments, Embed.embed_service.view(partner=partner, location=location, style=style))


  ## -- main execution flow -- ##
  def execute(arguments):

    """ Execute the `embed` tool, considering subtools. """

    output._apply_logging_settings(arguments)
    if arguments.subcommand == "data":
      return Embed.Data.execute(arguments)
    elif arguments.subcommand == "view":
      return Embed.View.execute(arguments)
    print "Invalid subcommand for 'embed' tool: '%s'." % arguments.subcommand
    exit(1)
