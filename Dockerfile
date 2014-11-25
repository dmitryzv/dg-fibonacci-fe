FROM python:3-onbuild

# Add and install Python modules
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt

# Bundle app source
ADD . /src

# Expose
EXPOSE 80

# Run
CMD ["python", "/src/application.py"]
