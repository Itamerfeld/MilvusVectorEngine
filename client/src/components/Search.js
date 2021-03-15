import React, { useState } from 'react'
import axios from 'axios'
import ReactJson from 'react-json-view'
import { FilePond, registerPlugin } from "react-filepond";
import "filepond/dist/filepond.min.css";
import FilePondPluginImageExifOrientation from "filepond-plugin-image-exif-orientation";
import FilePondPluginImagePreview from "filepond-plugin-image-preview";
import "filepond-plugin-image-preview/dist/filepond-plugin-image-preview.css";
import Annotation from 'react-image-annotation';
registerPlugin(FilePondPluginImageExifOrientation, FilePondPluginImagePreview);

export default function Search() {

    const [image ,setImage] = useState('')
    const [annotations , setAnnotations] = useState([])
    const [jsonData , setJsonData] = useState({'MVC':'MVC'})
    const [loading , setLoading] = useState(false)

    const sendRequest = (file , type) =>{
    const reader = new FileReader();
    reader.readAsDataURL(file.file);
    reader.onload = () => {
        let image = new Image();
        image.src = reader.result;
        image.onload = () => {
            setImage(image.src)
            setLoading(true)
            let data = new FormData()
            data.append('collection_name', 'koren')
            data.append('file', file.file)
            axios.post( 'http://localhost:5000/'+type+'?key=secret', data, {})
                .then(res => {
                    setJsonData(res.data)
                    setLoading(false)
                }).catch(error => {
                    setJsonData(JSON.parse(error))
                    setLoading(false)
                })
            };
        };
      }
    

    return (
        <div>
            {loading ? <div className="loading-page"><div className='loader' /></div> : ''}
            <div className='main'>
                <div className='main-form'>
                    <FilePond
                        allowMultiple={false}
                        allowReplace={false}
                        onaddfile={(err, file) => sendRequest(file , 'search_collection/')}
                        onremovefile={(err, file) => {
                        setAnnotations([])
                        setImage('')
                        setJsonData({'MVC':'MVC'})
                        }}
                    />
                    <ReactJson 
                    displayDataTypes={false} indentWidth={3} iconStyle={"circle"} style={{fontSize:'13px'}} 
                    src={jsonData} 
                    />
                </div>
            <div className='annotation-main'>
                <Annotation
                    src={image}
                    annotations={annotations}
                    value={{}}
                    disableOverlay={true}
                    style={{borderRadius:'5px'}}
                />
            </div>
            </div>
        </div>
    )
}
