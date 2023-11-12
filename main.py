from flask import Flask, render_template, request, redirect, url_for
import re
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/Creer/<Container_type><Container_name>', methods=['GET', 'POST'])
def Creer(Container_type,Container_name):
    client = docker.from_env()
    if request.method == 'POST':
        Container_name =re.sub(r'\s', '_',request.form.get('Container_name'))
        Base_Image = request.form.get('Base_Image')
        client.containers.create(image=Base_Image, name=Container_name,command="tail -f /dev/null", detach=True)
        return redirect(url_for('index'))


@app.route('/', methods=['GET', 'POST'])
def index():
    client = docker.from_env()
    images = client.images.list(all=True)
    containers = client.containers.list(all=True)
    return render_template('index.html', images=images, containers=containers)


@app.route('/Demarrer/<container_id>', methods=['POST'])
def Demarrer(container_id):
    client = docker.from_env()
    container = client.containers.get(container_id)
    container.start()
    return redirect(url_for('index'))

@app.route('/Arreter/<container_id>', methods=['POST'])
def Arreter(container_id):
    client = docker.from_env()
    try:
        container = client.containers.get(container_id)
        container.stop()
        return redirect(url_for('index'))
    except docker.errors.NotFound:
        return f'Container with ID {container_id} not found.'
    except docker.errors.ContainerError as e:
        return f"Impossible d'Arreter le conteneur {e}"
    except docker.errors.APIError as e:
        return redirect(url_for('error'), error=e)

@app.route('/Supprimer/<container_id>', methods=['POST'])
def Supprimer(container_id):
    client = docker.from_env()
    container = client.containers.get(container_id)
    if container.attrs['State']['Status'] != 'running':
        container.remove()
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
   

if __name__ == '__main__':
    app.run(debug=True)
