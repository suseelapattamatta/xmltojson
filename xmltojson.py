import streamlit as st
import json
import xmltodict

st.title("XML to JSON Converter")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  xml_file = uploaded_file.read()
  json_file = json_loads(json.dumps(xmltodict.parse(xml_file)))
  st.write(json_file)
else:
  st.text("No XML file uploaded")
