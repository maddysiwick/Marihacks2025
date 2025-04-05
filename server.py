from flask import Flask,jsonify
import tarfile
import tempfile

app=Flask('__name__')

@app.route('/')
def server():
#do i need a temp directory here and if i had one what would it do
    tar=tarfile.open('sendtar.tar.gz','w:gz')
    tar.add('Octoprint.usd')
    #return tar
    return jsonify({'message':'hello world!!!'})