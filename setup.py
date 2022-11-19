from setuptools import setup, find_packages


setup(

    name='Demoday Application',

    version='1.0',

    setup_requires=('wheel==0.37.0'),

   data_files=[('application/static/css', ['application/static/css/style.css']),

                ('application/static/js', ['application/static/js/script.js',]),

                ('application/templates', ['application/templates/test.html'])],

    packages=find_packages(),

    include_package_data=True,

    zip_safe=False,

    install_requires=[

        'click==8.0.3',

        'colorama==0.4.4',

        'Flask==2.0.2',

        'gunicorn==20.1.0',

        'itsdangerous==2.0.1',

        'Jinja2==3.0.3',

        'MarkupSafe==2.0.1',

        'Werkzeug==2.0.2'])
