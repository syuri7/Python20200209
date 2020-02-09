/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
!function(){const e=document.location.search.match(/\bid=([\w-]+)/)[1],a=new class{constructor(){this.handlers=new Map,window.addEventListener("message",e=>{if(e.data&&("onmessage"===e.data.command||"do-update-state"===e.data.command))return void this.postMessage(e.data.command,e.data.data);const a=e.data.channel,s=this.handlers.get(a);s?s(e,e.data.args):console.log("no handler for ",e)})}postMessage(a,s){window.parent.postMessage({target:e,channel:a,data:s},"*")}onMessage(e,a){this.handlers.set(e,a)}},s=new Promise(async e=>{if(!function(){try{return!!navigator.serviceWorker}catch(e){return!1}}())return console.log("Service Workers are not enabled. Webviews will not work properly"),e();navigator.serviceWorker.register("service-worker.js").then(async a=>{await navigator.serviceWorker.ready;const s=r=>{if("version"===r.data.channel)return navigator.serviceWorker.removeEventListener("message",s),1===r.data.version?e():a.update().then(()=>navigator.serviceWorker.ready).finally(e)}
;navigator.serviceWorker.addEventListener("message",s),a.active.postMessage({channel:"version"})});const s=e=>{a.onMessage(e,a=>{navigator.serviceWorker.ready.then(s=>{s.active.postMessage({channel:e,data:a.data.args})})})};s("did-load-resource"),s("did-load-localhost"),navigator.serviceWorker.addEventListener("message",e=>{["load-resource","load-localhost"].includes(e.data.channel)&&a.postMessage(e.data.channel,e.data)})});window.createWebviewManager({postMessage:a.postMessage.bind(a),onMessage:a.onMessage.bind(a),ready:s,fakeLoad:!0})}();
//# sourceMappingURL=https://ticino.blob.core.windows.net/sourcemaps/beaf391bc53136912e4f0bbdfb7844ad954247db/core/vs/workbench/contrib/webview/browser/pre/host.js.map
