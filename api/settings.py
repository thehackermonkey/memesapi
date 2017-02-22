DOMAIN ={
	'popular':{}
}

#popular memes schema
popular = {
	'item_title': 'A meme list',
	'cache_control': 'max-age=10,must-revalidate',
	'cache_expires': 10
}

popularchema ={
	"title": {'type': 'string'},
	"imgsrc": {'type': 'stringt'},
	"memeid": {'type': 'int'}
}

popular['schema'] = popularchema
DOMAIN['popular'] = popular


#display data only in json format
XML = False
EMBEDDING = True
HATEOAS = False

#mongo config
MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DBNAME = 'memes'




