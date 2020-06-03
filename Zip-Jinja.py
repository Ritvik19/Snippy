app = Flask(__name__)
...
app.jinja_env.filters['zip'] = zip


{% for value1, value2 in iterable1|zip(iterable2) %}
    {{ value1 }} is paired with {{ value2 }}
{% endfor %}