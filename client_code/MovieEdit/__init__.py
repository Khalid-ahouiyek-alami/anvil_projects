from ._anvil_designer import MovieEditTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class MovieEdit(MovieEditTemplate):
  def __init__(self, **properties):
  # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
    self.repeating_panel_1.items =  app_tables.movies.search()
    self.repeating_panel_1.add_event_handler('x-edit-movie', self.edit_movie)
    #add this line
    self.repeating_panel_1.add_event_handler('x-delete-movie', self.delete_movie)