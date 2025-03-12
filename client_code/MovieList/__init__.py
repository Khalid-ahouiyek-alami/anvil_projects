from ._anvil_designer import MovieListTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..MovieEdit import MovieEdit


class MovieList(MovieListTemplate):
  def _init_(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
    self.repeating_panel_1.items = app_tables.movies.search()
    #add this line to set the event handler
    self.repeating_panel_1.add_event_handler('x-edit-movie', self.edit_movie)

  def add_movie_click(self, **event_args):
    item = {}
    editing_form = MovieEdit(item=item)
    if alert(content=editing_form, large=True):
      #add the movie to the Data Table with the filled in information
      anvil.server.call('add_movie', item)
      #refresh the Data Grid
      self.repeating_panel_1.items = app_tables.movies.search()
  
  def edit_movie(self, movie, **event_args):
    #movie is the row from the Data Table
    item = dict(movie)
    editing_form = MovieEdit(item=item)
  
    #if the user clicks OK on the alert
    if alert(content=editing_form, large=True):
      #pass in the Data Table row and the updated info
      anvil.server.call('update_movie', movie, item)
      #refresh the Data Grid
      self.repeating_panel_1.items = app_tables.movies.search()