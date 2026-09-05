import * as React from 'react';

import './Editor.sass';
import { Api } from '../../libraries/api';


export default function Header() {
  const [content, saveContent] =
    React.useState('Using Python as backend, you can perform operations that are not allowed in Javascript, for example disk access. Click button below to save this content to hard drive.');

  return (
    <div className='editor-container'>
      <textarea className='textarea' value={content} onChange={(e) => {
        saveContent(e.target.value);
      }} /><br />

      <button className='button' onClick={() => {
        Api.saveContent(content);
      }}>Save</button>
    </div>
  );
}
