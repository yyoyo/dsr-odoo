#Create env
mkvirtualenv odoo
python setup.py install

#First Run server
createdb odoo
./openerp-server -d odoo -u base --addons=addons/,yoyo/

#Later on, to go back on env
workon odoo
./openerp-server -d odoo -u base --addons=addons/,yoyo/
