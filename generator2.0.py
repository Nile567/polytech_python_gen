def set_text_color(text_color='black'):
	return '''p{
    color: '''+text_color+''';
   } '''

def set_background_color(background_color='white'):
	return '''body{
    background-color: '''+background_color+''';
   } '''

def set_header_settings():
	return '''header{
    height: '''+input('Высота шапки: \n')+''';
    background: '''+input('Цвет шапки: \n')+''';
    text-align: left;
    padding-left: 10px;;
   } '''

def create_header():
	return '''
	<a id="logo">'''+input('Заголовок сайта: \n')+'''</a>
	'''

def create_content(filepath):
	if filepath=='':
		return '<p>'+input('Контент: \n')+'</p>'
	else:
		with open(filepath, 'r') as Content_file:
			return '<p>'+Content_file.read()+'</p>'
def create_html(file, title = '''Автоматически созданный сайт'''):
	file.write('''<!DOCTYPE html>
	
	
<html>
<head>
	<title>'''+title+'''</title>
	<style type="text/css">
	'''
	+set_background_color(input('Цвет фона страницы: \n'))
	+set_text_color(input('Цвет текста страницы: \n'))
	+set_header_settings()
	+'''
	#logo {
    display: block;
    padding: 0;
    font: bold 70px/60px 'PT Serif',Tahoma,Verdana,Segoe,sans-serif;
    color: '''+input('Цвет заголовка: \n')+''';
    text-decoration: none;
    letter-spacing: -.04em;
	}
	#header{
	height: 60px;
	margin: auto;
	}
	footer{
	background-color: #5000ff;
	color: #f7f1ef;
	text-align: center;
	}
	.content{
	border-style: solid;
    border-width: 1px;
    border-color: darkgrey;
	min-height: 768px;
	width: 1366px;
	margin: 0 auto;
	}
	#box{
	padding:40px;
	}
	</style>
</head>
<body>
<header>
<div id="box">
<div id="header">'''+create_header()+'''</div>
</div>
</header>
</body>
</html>''')

with open('gener.html', 's') as file:
	create_html(file, 'okey')
