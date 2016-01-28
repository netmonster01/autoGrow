import cherrypy
import os
songs = {
    '1': {
        'title': 'Lumberjack Song',
        'artist': 'Canadian Guard Choir'
    },

    '2': {
        'title': 'Always Look On the Bright Side of Life',
        'artist': 'Eric Idle'
    },

    '3': {
        'title': 'Spam Spam Spam',
        'artist': 'Monty Python'
    }
}


VIEWS_DIR = os.path.join(os.path.abspath("."), "static")
CSS_DIR = os.path.join(os.path.abspath("."), "css")
current_dir = os.path.dirname(os.path.abspath(__file__)) + os.path.sep

class GrowApi:

	exposed = True
	
	def POST(self, section, action):
		return ('Section:'+ section + ' Action: '+ action)

class Songs:

    exposed = True

    def GET(self, id=None):

        if id is None:
            return('Here are all the songs we have: %s' % songs)
        elif id in songs:
            song = songs[id]

            return(
                'Song with the ID %s is called %s, and the artist is %s' % (
                    id, song['title'], song['artist']))
        else:
            return('No song with the ID %s :-(' % id)

    def POST(self, title, artist):

        id = str(max([int(_) for _ in songs.keys()]) + 1)

        songs[id] = {
            'title': title,
            'artist': artist
        }

        return ('Create a new song with the ID: %s' % id)

    def PUT(self, id, title=None, artist=None):
        if id in songs:
            song = songs[id]

            song['title'] = title or song['title']
            song['artist'] = artist or song['artist']

            return(
                'Song with the ID %s is now called %s, '
                'and the artist is now %s' % (
                    id, song['title'], song['artist'])
            )
        else:
            return('No song with the ID %s :-(' % id)

    def DELETE(self, id):
        if id in songs:
            songs.pop(id)

            return('Song with the ID %s has been deleted.' % id)
        else:
            return('No song with the ID %s :-(' % id)

class RaspiGrowApp(object):

	@cherrypy.expose
	def index(self):
		print(VIEWS_DIR)
		return open(os.path.join(VIEWS_DIR, u'index.html')) #return "Hello world!"

	#@cherrypy.expose
	#def settings(self):
	#	print(VIEWS_DIR)
	#	return open(os.path.join(VIEWS_DIR, u'settings.html')) #return "Hello world!"


if __name__ == '__main__':

	config = {
    'global': {
        'environment': 'production',
        'log.screen': True,
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080,
        'engine.autoreload_on': True,
        'log.error_file': os.path.join(current_dir, 'errors.log'),
        'log.access_file': os.path.join(current_dir, 'access.log'),
    },
    '/':{
        'tools.staticdir.root' : current_dir,
    },
    '/static':{
        'tools.staticdir.on' : True,
        'tools.staticdir.dir' : 'static',
    },
}
	#config = {'/':
 #               {
	#				'tools.staticdir.debug': True,
	#				'tools.staticdir.on': True,
	#				'log.screen': True,
	#				'tools.staticdir.dir': VIEWS_DIR,
 #               }
 #   }
	#cssconfig = {'/css':
 #               {
	#				'tools.staticdir.debug': True,
	#				'tools.staticdir.on': True,
	#				'log.screen': True,
	#				'tools.staticdir.dir': CSS_DIR,
 #               }
 #   }
	#cherrypy.tree.mount(Songs(), '/api/songs',{'/':{'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})
	#cherrypy.tree.mount(GrowApi(), '/api/growApi',{'/':{'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})
	cherrypy.quickstart(RaspiGrowApp(), '/', config)
	#cherrypy.tree.mount(RaspiGrowApp(), '/', 'C:\\Users\\kscavitt.CORP\\Documents\\visual studio 2015\\Projects\\raspiGrow\\raspiGrow\\app.config')
cherrypy.engine.start()
cherrypy.engine.block()
