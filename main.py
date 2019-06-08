from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.garden.mapview import MapView, MapMarker

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Show me on the map'
            on_press: root.manager.current = 'showme'
        Button:
            text: 'Another function'
            on_press: root.manager.current = 'flags'

<ShowMeScreen>:
    search_lat: coor_lat
	search_long: coor_long
	my_map: map
	my_image: image
    GridLayout:
        rows: 4
        cols: 1
        BoxLayout:
            size_hint_y: 1
            MapView:
                lat: 47
                lon: 5
                zoom: 3
                id: map
            Image:
                source: 'warszawa.jpg'
                id: image
        BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Lat"
    		Label:
    			size_hint_x: 25
    			id: coor_lat
    		Label:
    			size_hint_x: 25
    			text: "Long"
    		Label:
    			size_hint_x: 25
    			id: coor_long
    	BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Score"
    		Label:
    			size_hint_x: 25
    			text: '0'
    		Button:
    			size_hint_x: 25
    			text: "Check"
    			on_press: root.check_points()
    		Button:
    			size_hint_x: 25
    			text: "Next"
                on_press: root.manager.current = 'showme2'
        BoxLayout:
            size_hint_y: 0.1
            Button:
                height: "40dp"
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'
                
<ShowMe2Screen>:
    search_lat: coor_lat
	search_long: coor_long
	my_map: map
	my_image: image2
    GridLayout:
        rows: 4
        cols: 1
        BoxLayout:
            size_hint_y: 1
            MapView:
                lat: 0
                lon: 0
                zoom: 1
                id: map
            Image:
                source: 'wenecja.jpg'
                id: image2
        BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Lat"
    		Label:
    			size_hint_x: 25
    			id: coor_lat
    		Label:
    			size_hint_x: 25
    			text: "Long"
    		Label:
    			size_hint_x: 25
    			id: coor_long
    	BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Score"
    		Label:
    			size_hint_x: 25
    			text: '0'
    		Button:
    			size_hint_x: 25
    			text: "Check"
    			on_press: root.check_points()
            Button:
    			size_hint_x: 25
    			text: "Back"
                on_press: root.manager.current = 'showme'
    		Button:
    			size_hint_x: 25
    			text: "Next"
                on_press: root.manager.current = 'showme3'
        BoxLayout:
            size_hint_y: 0.1
            Button:
                height: "40dp"
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'
            
<ShowMe3Screen>:
    search_lat: coor_lat
	search_long: coor_long
	my_map: map
	my_image: image3
    GridLayout:
        rows: 4
        cols: 1
        BoxLayout:
            size_hint_y: 1
            MapView:
                lat: 0
                lon: 0
                zoom: 1
                id: map
            Image:
                source: 'Giza.jpg'
                id: image3
        BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Lat"
    		Label:
    			size_hint_x: 25
    			id: coor_lat
    		Label:
    			size_hint_x: 25
    			text: "Long"
    		Label:
    			size_hint_x: 25
    			id: coor_long
    	BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Score"
    		Label:
    			size_hint_x: 25
    			text: '0'
    		Button:
    			size_hint_x: 25
    			text: "Check"
    			on_press: root.check_points()
            Button:
    			size_hint_x: 25
    			text: "Back"
                on_press: root.manager.current = 'showme2'
    		Button:
    			size_hint_x: 25
    			text: "Next"
                on_press: root.manager.current = 'showme4'
        BoxLayout:
            size_hint_y: 0.1
            Button:
                height: "40dp"
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'
                
<ShowMe4Screen>:
    search_lat: coor_lat
	search_long: coor_long
	my_map: map
	my_image: image4
    GridLayout:
        rows: 4
        cols: 1
        BoxLayout:
            size_hint_y: 1
            MapView:
                lat: 0
                lon: 0
                zoom: 1
                id: map
            Image:
                source: 'londyn.jpg'
                id: image4
        BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Lat"
    		Label:
    			size_hint_x: 25
    			id: coor_lat
    		Label:
    			size_hint_x: 25
    			text: "Long"
    		Label:
    			size_hint_x: 25
    			id: coor_long
    	BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Score"
    		Label:
    			size_hint_x: 25
    			text: '0'
    		Button:
    			size_hint_x: 25
    			text: "Check"
    			on_press: root.check_points()
            Button:
    			size_hint_x: 25
    			text: "Back"
                on_press: root.manager.current = 'showme3'
    		Button:
    			size_hint_x: 25
    			text: "Next"
                on_press: root.manager.current = 'showme5'
        BoxLayout:
            size_hint_y: 0.1
            Button:
                height: "40dp"
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'

<ShowMe5Screen>:
    search_lat: coor_lat
	search_long: coor_long
	my_map: map
	my_image: image5
    GridLayout:
        rows: 4
        cols: 1
        BoxLayout:
            size_hint_y: 1
            MapView:
                lat: 0
                lon: 0
                zoom: 1
                id: map
            Image:
                source: 'rzym.jpeg'
                id: image5
        BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Lat"
    		Label:
    			size_hint_x: 25
    			id: coor_lat
    		Label:
    			size_hint_x: 25
    			text: "Long"
    		Label:
    			size_hint_x: 25
    			id: coor_long
    	BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Score"
    		Label:
    			size_hint_x: 25
    			text: '0'
    		Button:
    			size_hint_x: 25
    			text: "Check"
    			on_press: root.check_points()
            Button:
    			size_hint_x: 25
    			text: "Back"
                on_press: root.manager.current = 'showme4'
    		Button:
    			size_hint_x: 25
    			text: "Next"
                on_press: root.manager.current = 'showme6'
        BoxLayout:
            size_hint_y: 0.1
            Button:
                height: "40dp"
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'
                
<ShowMe6Screen>:
    search_lat: coor_lat
	search_long: coor_long
	my_map: map
	my_image: image6
    GridLayout:
        rows: 4
        cols: 1
        BoxLayout:
            size_hint_y: 1
            MapView:
                lat: 0
                lon: 0
                zoom: 1
                id: map
            Image:
                source: 'barcelona.jpg'
                id: image6
        BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Lat"
    		Label:
    			size_hint_x: 25
    			id: coor_lat
    		Label:
    			size_hint_x: 25
    			text: "Long"
    		Label:
    			size_hint_x: 25
    			id: coor_long
    	BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Score"
    		Label:
    			size_hint_x: 25
    			text: '0'
    		Button:
    			size_hint_x: 25
    			text: "Check"
    			on_press: root.check_points()
            Button:
    			size_hint_x: 25
    			text: "Back"
                on_press: root.manager.current = 'showme5'
    		Button:
    			size_hint_x: 25
    			text: "Next"
                on_press: root.manager.current = 'showme7'
        BoxLayout:
            size_hint_y: 0.1
            Button:
                height: "40dp"
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'

<ShowMe7Screen>:
    search_lat: coor_lat
	search_long: coor_long
	my_map: map
	my_image: image7
    GridLayout:
        rows: 4
        cols: 1
        BoxLayout:
            size_hint_y: 1
            MapView:
                lat: 0
                lon: 0
                zoom: 1
                id: map
            Image:
                source: 'oslo.jpg'
                id: image7
        BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Lat"
    		Label:
    			size_hint_x: 25
    			id: coor_lat
    		Label:
    			size_hint_x: 25
    			text: "Long"
    		Label:
    			size_hint_x: 25
    			id: coor_long
    	BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Score"
    		Label:
    			size_hint_x: 25
    			text: '0'
    		Button:
    			size_hint_x: 25
    			text: "Check"
    			on_press: root.check_points()
            Button:
    			size_hint_x: 25
    			text: "Back"
                on_press: root.manager.current = 'showme6'
    		Button:
    			size_hint_x: 25
    			text: "Next"
                on_press: root.manager.current = 'showme8'
        BoxLayout:
            size_hint_y: 0.1
            Button:
                height: "40dp"
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'
                
<ShowMe8Screen>:
    search_lat: coor_lat
	search_long: coor_long
	my_map: map
	my_image: image8
    GridLayout:
        rows: 4
        cols: 1
        BoxLayout:
            size_hint_y: 1
            MapView:
                lat: 0
                lon: 0
                zoom: 1
                id: map
            Image:
                source: 'tokio.jpg'
                id: image8
        BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Lat"
    		Label:
    			size_hint_x: 25
    			id: coor_lat
    		Label:
    			size_hint_x: 25
    			text: "Long"
    		Label:
    			size_hint_x: 25
    			id: coor_long
    	BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Score"
    		Label:
    			size_hint_x: 25
    			text: '0'
    		Button:
    			size_hint_x: 25
    			text: "Check"
    			on_press: root.check_points()
            Button:
    			size_hint_x: 25
    			text: "Back"
                on_press: root.manager.current = 'showme7'
    		Button:
    			size_hint_x: 25
    			text: "Next"
                on_press: root.manager.current = 'showme9'
        BoxLayout:
            size_hint_y: 0.1
            Button:
                height: "40dp"
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'

<ShowMe9Screen>:
    search_lat: coor_lat
	search_long: coor_long
	my_map: map
	my_image: image9
    GridLayout:
        rows: 4
        cols: 1
        BoxLayout:
            size_hint_y: 1
            MapView:
                lat: 0
                lon: 0
                zoom: 1
                id: map
            Image:
                source: 'moskwa.jpg'
                id: image9
        BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Lat"
    		Label:
    			size_hint_x: 25
    			id: coor_lat
    		Label:
    			size_hint_x: 25
    			text: "Long"
    		Label:
    			size_hint_x: 25
    			id: coor_long
    	BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Score"
    		Label:
    			size_hint_x: 25
    			text: '0'
    		Button:
    			size_hint_x: 25
    			text: "Check"
    			on_press: root.check_points()
            Button:
    			size_hint_x: 25
    			text: "Back"
                on_press: root.manager.current = 'showme8'
    		Button:
    			size_hint_x: 25
    			text: "Next"
                on_press: root.manager.current = 'showme10'
        BoxLayout:
            size_hint_y: 0.1
            Button:
                height: "40dp"
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'
                
<ShowMe10Screen>:
    search_lat: coor_lat
	search_long: coor_long
	my_map: map
	my_image: image10
    GridLayout:
        rows: 4
        cols: 1
        BoxLayout:
            size_hint_y: 1
            MapView:
                lat: 0
                lon: 0
                zoom: 1
                id: map
            Image:
                source: 'rio.jpg'
                id: image10
        BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Lat"
    		Label:
    			size_hint_x: 25
    			id: coor_lat
    		Label:
    			size_hint_x: 25
    			text: "Long"
    		Label:
    			size_hint_x: 25
    			id: coor_long
    	BoxLayout:
    		size_hint_y: 0.1
    		Label:
    			size_hint_x: 25
    			text: "Score"
    		Label:
    			size_hint_x: 25
    			text: '0'
    		Button:
    			size_hint_x: 25
    			text: "Check"
    			on_press: root.check_points()
            Button:
    			size_hint_x: 25
    			text: "Back"
                on_press: root.manager.current = 'showme9'
    		Button:
    			size_hint_x: 25
    			text: "Zakończ"
        BoxLayout:
            size_hint_y: 0.1
            Button:
                height: "40dp"
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'
                
<FlagsScreen>:
    BoxLayout:
        Label:
            text: 'Czy to wystarczy na 20% z projektu? :D'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class ShowMeScreen(Screen):
    def __init__(self, **kwargs):
        super(ShowMeScreen, self).__init__(**kwargs)

        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
#class ShowMeScreen(Screen):
#    def draw_marker(self):
#        
#        try:
#            self.my_map.remove_marker(self.marker)
#        except:
#            pass
#        
#        self.latitude = self.my_map.lat
#        self.longitude = self.my_map.lon
#        
#        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
#        self.my_map.add_marker(self.marker)
#        
#        self.search_lat.text = "{}".format(self.latitude)
#        self.search_long.text = "{}".format(self.longitude)
#        
class ShowMe2Screen(Screen):
    def __init__(self, **kwargs):
        super(ShowMe2Screen, self).__init__(**kwargs)

        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        
class ShowMe3Screen(Screen):
    def __init__(self, **kwargs):
        super(ShowMe3Screen, self).__init__(**kwargs)

        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        
class ShowMe4Screen(Screen):
    def __init__(self, **kwargs):
        super(ShowMe4Screen, self).__init__(**kwargs)

        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        
    def check_points(self):
        print(list_of_points[0][0])
        if self.my_image.source == list_of_points[0][0]:
            print("wynik")

class ShowMe5Screen(Screen):
    def __init__(self, **kwargs):
        super(ShowMe5Screen, self).__init__(**kwargs)

        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        
class ShowMe6Screen(Screen):
    def __init__(self, **kwargs):
        super(ShowMe6Screen, self).__init__(**kwargs)

        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)

class ShowMe7Screen(Screen):
    def __init__(self, **kwargs):
        super(ShowMe7Screen, self).__init__(**kwargs)

        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        
class ShowMe8Screen(Screen):
    def __init__(self, **kwargs):
        super(ShowMe8Screen, self).__init__(**kwargs)

        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)

class ShowMe9Screen(Screen):
    def __init__(self, **kwargs):
        super(ShowMe9Screen, self).__init__(**kwargs)

        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        
class ShowMe10Screen(Screen):
    def __init__(self, **kwargs):
        super(ShowMe10Screen, self).__init__(**kwargs)

        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        
class FlagsScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ShowMeScreen(name='showme'))
sm.add_widget(ShowMe2Screen(name='showme2'))
sm.add_widget(ShowMe3Screen(name='showme3'))
sm.add_widget(ShowMe4Screen(name='showme4'))
sm.add_widget(ShowMe5Screen(name='showme5'))
sm.add_widget(ShowMe6Screen(name='showme6'))
sm.add_widget(ShowMe7Screen(name='showme7'))
sm.add_widget(ShowMe8Screen(name='showme8'))
sm.add_widget(ShowMe9Screen(name='showme9'))
sm.add_widget(ShowMe10Screen(name='showme10'))
sm.add_widget(FlagsScreen(name='flags'))
list_of_points = [
                ['warszawa.jpg', 52.2297700, 21.0117800],
                ['wenecja.jpg', 45.4371300, 12.3326500],
                ['Giza.jpg', 30.0080800, 31.2109300],
                ['londyn.jpg', 51.5085300, -0.1257400],
                ['rzym.jpeg', 41.8919300, 12.5113300],
                ['barcelona.jpg', 41.3887900, 2.1589900],
                ['oslo.jpg', 59.9127300, 10.7460900],
                ['tokio.jpg', 35.6895000, 139.6917100],
                ['moskwa.jpg', 55.7522200, 37.6155600],
                ['rio.jpg', -22.9027800, -43.2075000],
                ]

class multipleScreens(App):

    def build(self):
        return sm

if __name__ == '__main__':
    multipleScreens().run()