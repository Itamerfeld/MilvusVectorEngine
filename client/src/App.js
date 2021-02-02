import React, { Component } from 'react'
import axios from 'axios'
import ReactJson from 'react-json-view'
import IMG from './search.png'
import { FilePond, registerPlugin } from "react-filepond";
import "filepond/dist/filepond.min.css";
import FilePondPluginImageExifOrientation from "filepond-plugin-image-exif-orientation";
import FilePondPluginImagePreview from "filepond-plugin-image-preview";
import "filepond-plugin-image-preview/dist/filepond-plugin-image-preview.css";
import Annotation from 'react-image-annotation';
registerPlugin(FilePondPluginImageExifOrientation, FilePondPluginImagePreview);

export default class App extends Component {

  state = {
    file : undefined,
    loading: false,
    selectedFile: '',
    JsonData: {'Type':'VectorComparison'},
    image:IMG,
  }

  sendRequest = (file , type) =>{
    const reader = new FileReader();
                            reader.readAsDataURL(file.file);
                            reader.onload = () => {
                                let image = new Image();
                                image.src = reader.result;
                                image.onload = () => {
                                    this.setState({image:image.src , loading: true , selectedFile: file.file})
                                    const data = new FormData()
                                    data.append('collection_name', 'koren')
                                    data.append('file', this.state.selectedFile)
                                    axios.post( 'http://localhost:5000/'+type, data, {})
                                      .then(res => {
                                        this.setState({ JsonData: res.data , loading: false })
                                      }).catch(error => {
                                        this.setState({ JsonData: JSON.parse(error), selectedFile: '', loading: false })
                                      })
                                };
                            };
  }
 
  render() {
    return (
      <div>
        {this.state.loading ? <div className="loading-page"><div className='loader' /></div> : ''}
        <div className='main-flex'>
          <div className='form-main'>
          <h3>Upload</h3>
          <FilePond
                        allowMultiple={false}
                        allowReplace={false}
                        onaddfile={(err, file) => {this.sendRequest(file , 'insert_collection/')}}
                        onremovefile={(err, file) => {
                          this.setState({selectedFile:'' , annotations:[] ,  JsonData:{'Algorithm':'Objects Detection'}, image:IMG , anotations:[]})
                      }}
                        />
            <h3>Search</h3>
            <FilePond
                        allowMultiple={false}
                        allowReplace={false}
                        onaddfile={(err, file) => {this.sendRequest(file , 'search_collection/')}}
                        onremovefile={(err, file) => {
                          this.setState({selectedFile:'' , annotations:[] ,  JsonData:{'Algorithm':'Objects Detection'}, image:IMG , anotations:[]})
                      }}
                        />
            <ReactJson displayDataTypes={false} indentWidth={3} iconStyle={"circle"} style={{fontSize:'13px'}} src={this.state.JsonData} />
          </div>
          <div className='annotation-main'>
          <Annotation
            src={this.state.image}
            annotations={[]}
            value={{}}
            disableOverlay={true}
            />
          </div>
        </div>
      </div>
    )
  }
}