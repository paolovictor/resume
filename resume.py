#!/usr/bin/python
# coding: utf-8

basic = {
	'name': u'Paolo Soares',
	'trade': u'Software engineer',
	'email': u'paolovictor@gmail.com',
	'phone': u'+55 48 96883508',
	'cover': "I'm a passionate software engineer with a mission: develop software that \
	          actually impacts people's lives in a positive way. Anything less is a distraction.",
	'linkedin': u'http://br.linkedin.com/pub/paolo-victor/16/20a/128/',
	'url': u'http://www.paolovictor.com'
}

cover_letter_count = len(basic['cover'].split(' '))

buzzword_soup = ['Java', 'Python', 'C', 'Javascript', 'Scala']

education = [
	{
	    'when': u'2008 - 2010',
		'title': u'MsC',
		'area': u'Computer Science',
		'where': u'Universidade Federal de Minas Gerais - UFMG',
		'url': u'http://www.dcc.ufmg.br/pos',
		'spec': u'Network Virtualization',
		'work_title': u'Distributed Network Traffic Control in Virtualized Data Centers',
		'advisor': u'Dorgival Guedes Neto'
	},
	{
	    'when': u'2003 - 2007',
		'title': u'BsC',
		'area': u'Computer Science',
		'where': u'Universidade Federal de Campina Grande - UFCG',
		'url': u'http://www.ufcg.edu.br',
		'spec': u'Distributed Systems'
	},
]

experience = [
	{
	    'when': u'May 2012 - Present',
		'where': u'Chaordic Systems',
		'what': u'Software engineer',
		'url': u'http://www.chaordic.com.br/en/?hl=en-us',
		'description': "Participated on the design and implementation of a highly scalable and flexible \
		                platform for configuring, monitoring and delivering personalized e-mail \
		                marketing campaigns for thousands of clients, based on their activities on some \
		                of Brazil's largest e-commerce companies. Besides working on the platform's backend \
		                and client activity analysis algorithms, I also worked on the development, sales process \
		                and deploy of new e-mail marketing campaigns. On a 7-month time frame, our team \
		                achieved a growth in aggregate sales from around R$ 600K per month to R$ 8.6 million."
	},
	{
	    'when': u'November 2011 - September 2012',
		'where': u'Distributed Systems Lab (LSD) at UFCG',
		'what': u'Software engineer',
		'url': u'http://www.lsd.ufcg.edu.br',
		'description': "Participated on the design and implementation of a portal for creating and \
		                running scientific workflows, with a twist: users with special permissions \
		                could create sub-portals for specific workflows, hiding the configuration \
		                and maintenance complexity from less tech-savvy users. The implementation \
		                effort also included developing a software bridge between the web backend \
		                and CSGrid, a distributed algorithm execution middleware, and developing a \
		                tool for converting CSGrid's algorithm definitions into tool definitions \
		                compatible with the web backend."
	},
	{
	    'when': u'July 2010 – November 2011',
		'where': u'Concert Technologies',
		'what': u'Software engineer',
		'url': u'http://www.concert.com.br/en/index_en.html',
		'description': "Designed and developed a mission-critical real-time monitoring system for \
						for the Brazilian Space Agency (AEB); Implemented a RESTful web service that \
						exposed data from a C legacy system, including C and Java modules which \
						communicated using ZeroMQ and Google's Protocol Buffers; Designed and acted as \
						a technical advisor on the development of a distributed, extensible \
						data collector for risk management systems; Worked on the implementation of a \
						desktop application for energy consumption analysis and forecasting."
	},
	{
	    'when': u'February 2008 – May 2010',
		'where': u'Universidade Federal de Minas Gerais - UFMG',
		'what': u'Msc student',
		'url': u'http://www.dcc.ufmg.br/pos',
		'description': u'Developed a traffic control technology to deal with unresponsive \
					    protocols on virtualized environments, including a implementation \
					    based on the Xen virtualization environment; Analyzed the link \
					    between content popularity and user social network size on social news websites.'
	},
	{
	    'when': u'July 2009 - December 2009',
		'where': u'Hewlett-Packard Labs',
		'what': u'Research Intern',
		'url': u'http://hpl.hp.com',
		'description': u'Developed a software-based traffic control solution for \
					    virtualized data centers, that handles both responsive and \
					    unresponsive traffic. The core of the solution prototype lies on a software \
					    agent running on a Xen Dom0 with a modified kernel hypervisor, which coordinates \
					    with the other virtual machines on the network to control unresponsive traffic.'
	},
	{
	    'when': u'2004 - 2008',
		'where': u'Distributed Systems Lab (LSD) at UFCG',
		'what': u'Research Assistant',
		'url': u'http://www.lsd.ufcg.edu.br',
		'description': u'Implemented a web portal for the execution of weather \
		 			    forecasts using a peer-to-peer grid middleware; \
		                Worked on a peer-to-peer backup system based on social networks; \
		                Designed a quota mechanism for the aforementioned system that \
		                employed a distributed reputation mechanism.'
	},
]

publications = [
	{
		'title': u'Isolamento de Tráfego em Ambientes Virtualizados',
		'title_alt': u'Traffic Isolation on Virtualized Environments',
		'authors': u'Henrique Rodrigues, Paolo Soares, Jose Renato Santos, Yoshio Turner, Dorgival Guedes',
		'where': u'Brazilian Symposium on Computer Networks - SBRC 2011'
	},
	{
		'title': u'Gatekeeper: Supporting Bandwidth Guarantees for Multi-tenant Datacenter Networks',
		'authors': u'Henrique Rodrigues, Jose Renato Santos, Yoshio Turner, Paolo Soares, Dorgival Guedes',
		'where': u'3rd Workshop on I/O Virtualization - USENIX 2011'
	},
	{
		'title': u'Solomon: Incentivando o Compartilhamento e Maior Disponibilidade em Sistemas de Armazenamento Entre-Pares',
		'title_alt': u'Solomon: Encouraging Sharing and High Availability on Peer-to-per Storage Systems',
		'authors': u'Paolo Soares, Marcelo Iury S. Oliveira, Dalton Serey Guerrero, Francisco Brasileiro',
		'where': u'WP2P - Workshop on P2P Systems  - Brazilian Symposium on Computer Networks - SBRC 2008'
	},
]

if __name__ == '__main__':
	import codecs

	from jinja2 import Template

	with codecs.open('template.html', 'r', 'utf-8') as template_file:
		template = Template(template_file.read())
		print template.render(basic = basic,
			  		          buzzword_soup = buzzword_soup,
			                  experience = experience,
			            	  education = education,
			            	  publications = publications,
			            	  cover_letter_count=cover_letter_count).encode('utf-8')