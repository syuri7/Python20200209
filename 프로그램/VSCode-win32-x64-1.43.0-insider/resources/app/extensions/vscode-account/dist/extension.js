!function(e,t){for(var n in t)e[n]=t[n]}(exports,function(e){var t={};function n(o){if(t[o])return t[o].exports;var r=t[o]={i:o,l:!1,exports:{}};return e[o].call(r.exports,r,r.exports,n),r.l=!0,r.exports}return n.m=e,n.c=t,n.d=function(e,t,o){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:o})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var o=Object.create(null);if(n.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)n.d(o,r,function(t){return e[t]}.bind(null,r));return o},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="",n(n.s=2)}([function(e,t){e.exports=require("vscode")},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});const o=n(0);function r(e,t,n=" "){return n.repeat(Math.max(0,t-e.length))+e}const s=new class{constructor(){this.output=o.window.createOutputChannel("Account")}data2String(e){return e instanceof Error?e.stack||e.message:!1===e.success&&e.message?e.message:e.toString()}info(e,t){this.logLevel("Info",e,t)}error(e,t){this.logLevel("Error",e,t)}logLevel(e,t,n){this.output.appendLine(`[${e}  - ${this.now()}] ${t}`),n&&this.output.appendLine(this.data2String(n))}now(){const e=new Date;return r(e.getUTCHours()+"",2,"0")+":"+r(e.getMinutes()+"",2,"0")+":"+r(e.getUTCSeconds()+"",2,"0")+"."+e.getMilliseconds()}};t.default=s},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});const o=n(0),r=n(3);t.activate=async function(e){const t=new r.AzureActiveDirectoryService;await t.initialize(),o.authentication.registerAuthenticationProvider({id:"MSA",displayName:"Microsoft",onDidChangeSessions:r.onDidChangeSessions.event,getSessions:()=>Promise.resolve(t.sessions),login:async e=>{try{return await t.login(e.sort().join(" ")),t.sessions[0]}catch(e){throw o.window.showErrorMessage(`Logging in failed: ${e}`),e}},logout:async e=>t.logout(e)})},t.deactivate=function(){}},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});const o=n(4),r=n(5),s=n(6),i=n(0),a=n(7),c=n(12),u=n(1),d=n(14),l="https://vscode-redirect.azurewebsites.net/",h="https://login.microsoftonline.com/",f="aebc6443-996d-45c2-90f0-388ff96faa56",p="organizations";t.onDidChangeSessions=new i.EventEmitter,t.REFRESH_NETWORK_FAILURE="Network failure";class g extends i.EventEmitter{handleUri(e){this.fire(e)}}t.AzureActiveDirectoryService=class{constructor(){this._tokens=[],this._refreshTimeouts=new Map,this._uriHandler=new g,i.window.registerUriHandler(this._uriHandler)}async initialize(){const e=await c.keychain.getToken();if(e)try{const t=this.parseStoredData(e),n=Object.create(null),o=t.filter(e=>!n[e.id]&&(n[e.id]=!0,!0)).map(async e=>{try{await this.refreshToken(e.refreshToken,e.scope)}catch(t){this.handleTokenRefreshFailure(t,e.id,e.refreshToken,e.scope,!1)}});await Promise.all(o)}catch(e){await this.clearSessions()}this.pollForChange()}parseStoredData(e){return JSON.parse(e)}async storeTokenData(){const e=this._tokens.map(e=>({id:e.sessionId,refreshToken:e.refreshToken,scope:e.scope}));await c.keychain.setToken(JSON.stringify(e))}pollForChange(){setTimeout(async()=>{let e=!1;const n=await c.keychain.getToken();if(n)try{const t=this.parseStoredData(n);let o=t.map(async t=>{if(!this._tokens.some(e=>e.scope===t.scope&&e.sessionId===t.id))try{await this.refreshToken(t.refreshToken,t.scope),e=!0}catch(e){this.handleTokenRefreshFailure(e,t.id,t.refreshToken,t.scope,!1)}});o=o.concat(this._tokens.map(async n=>{t.some(e=>n.scope===e.scope&&n.sessionId===e.id)||(await this.logout(n.sessionId),e=!0)})),await Promise.all(o)}catch(t){u.default.error(t.message),this.clearSessions(),e=!0}else this._tokens.length&&(await this.clearSessions(),e=!0);e&&t.onDidChangeSessions.fire(),this.pollForChange()},3e4)}convertToSession(e){return{id:e.sessionId,accessToken:()=>Promise.resolve(e.accessToken),accountName:e.accountName,scopes:e.scope.split(" ")}}getTokenClaims(e){try{return JSON.parse(Buffer.from(e.split(".")[1],"base64").toString())}catch(e){throw u.default.error(e.message),new Error("Unable to read token claims")}}get sessions(){return this._tokens.map(e=>this.convertToSession(e))}async login(e){if(u.default.info("Logging in..."),i.env.uiKind===i.UIKind.Web)return void await this.loginWithoutLocalServer(e);const t=o.randomBytes(16).toString("base64"),{server:n,redirectPromise:r,codePromise:s}=a.createServer(t);let c;try{const g=await a.startServer(n);i.env.openExternal(i.Uri.parse(`http://localhost:${g}/signin?nonce=${encodeURIComponent(t)}`));const m=await r;if("err"in m){const{err:e,res:t}=m;throw t.writeHead(302,{Location:`/?error=${encodeURIComponent(e&&e.message||"Unknown error")}`}),t.end(),e}const y=m.req.headers.host||"",w=(/^[^:]+:(\d+)$/.exec(Array.isArray(y)?y[0]:y)||[])[1],k=`${w?parseInt(w,10):g},${encodeURIComponent(t)}`,v=d.toBase64UrlEncoding(o.randomBytes(32).toString("base64")),T=d.toBase64UrlEncoding(o.createHash("sha256").update(v).digest("base64")),_=`${h}${p}/oauth2/v2.0/authorize?response_type=code&response_mode=query&client_id=${encodeURIComponent(f)}&redirect_uri=${encodeURIComponent(l)}&state=${k}&scope=${encodeURIComponent(e)}&prompt=select_account&code_challenge_method=S256&code_challenge=${T}`;await m.res.writeHead(302,{Location:_}),m.res.end();const S=await s,E=S.res;try{if("err"in S)throw S.err;c=await this.exchangeCodeForToken(S.code,v,e),this.setToken(c,e),u.default.info("Login successful"),E.writeHead(302,{Location:"/"}),E.end()}catch(e){u.default.error(e.message),E.writeHead(302,{Location:`/?error=${encodeURIComponent(e&&e.message||"Unknown error")}`}),E.end()}}catch(t){u.default.error(t.message),"Error listening to server"!==t.message&&"Closed"!==t.message&&"Timeout waiting for port"!==t.message||await this.loginWithoutLocalServer(e)}finally{setTimeout(()=>{n.close()},5e3)}}getCallbackEnvironment(e){switch(e.authority){case"online.visualstudio.com,":return"vso";case"online-ppe.core.vsengsaas.visualstudio.com":return"vsoppe,";case"online.dev.core.vsengsaas.visualstudio.com":return"vsodev,";default:return""}}async loginWithoutLocalServer(e){const t=await i.env.asExternalUri(i.Uri.parse(`${i.env.uriScheme}://vscode.vscode-account`)),n=o.randomBytes(16).toString("base64"),r=(t.authority.match(/:([0-9]*)$/)||[])[1]||("https"===t.scheme?443:80),s=`${this.getCallbackEnvironment(t)}${r},${encodeURIComponent(n)},${encodeURIComponent(t.query)}`,a=`${h}${p}/oauth2/v2.0/authorize`;let c=i.Uri.parse(a);const u=d.toBase64UrlEncoding(o.randomBytes(32).toString("base64")),g=d.toBase64UrlEncoding(o.createHash("sha256").update(u).digest("base64"));c=c.with({query:`response_type=code&client_id=${encodeURIComponent(f)}&response_mode=query&redirect_uri=${l}&state=${s}&scope=${e}&prompt=select_account&code_challenge_method=S256&code_challenge=${g}`}),i.env.openExternal(c);const m=new Promise((e,t)=>{const n=setTimeout(()=>{clearTimeout(n),t("Login timed out.")},3e5)});return Promise.race([this.handleCodeResponse(s,u,e),m])}async handleCodeResponse(e,t,n){let o;return new Promise((r,s)=>{o=this._uriHandler.event(async o=>{try{const i=function(e){return e.query.split("&").reduce((e,t)=>{const n=t.split("=");return e[n[0]]=n[1],e},{})}(o),a=i.code;if(i.state!==e)throw new Error("State does not match.");const c=await this.exchangeCodeForToken(a,t,n);this.setToken(c,n),r(c)}catch(e){s(e)}})}).then(e=>(o.dispose(),e)).catch(e=>{throw o.dispose(),e})}async setToken(e,n){const o=this._tokens.findIndex(t=>t.sessionId===e.sessionId);o>-1?this._tokens.splice(o,1,e):this._tokens.push(e),this.clearSessionTimeout(e.sessionId),this._refreshTimeouts.set(e.sessionId,setTimeout(async()=>{try{await this.refreshToken(e.refreshToken,n),t.onDidChangeSessions.fire()}catch(t){this.handleTokenRefreshFailure(t,e.sessionId,e.refreshToken,n,!0)}},1e3*(parseInt(e.expiresIn)-30))),this.storeTokenData()}getTokenFromResponse(e,t){const n=JSON.parse(Buffer.concat(e).toString()),o=this.getTokenClaims(n.access_token);return{expiresIn:n.expires_in,accessToken:n.access_token,refreshToken:n.refresh_token,scope:t,sessionId:`${o.tid}/${o.oid||o.altsecid||""+o.ipd||""}/${t}`,accountName:o.email||o.unique_name||"user@example.com"}}async exchangeCodeForToken(e,t,n){return new Promise((o,a)=>{u.default.info("Exchanging login code for token");try{const c=s.stringify({grant_type:"authorization_code",code:e,client_id:f,scope:n,code_verifier:t,redirect_uri:l}),d=i.Uri.parse(`${h}${p}/oauth2/v2.0/token`),g=r.request({host:d.authority,path:d.path,method:"POST",headers:{"Content-Type":"application/x-www-form-urlencoded","Content-Length":c.length}},e=>{const t=[];e.on("data",e=>{t.push(e)}),e.on("end",()=>{200===e.statusCode?(u.default.info("Exchanging login code for token success"),o(this.getTokenFromResponse(t,n))):(u.default.error("Exchanging login code for token failed"),a(new Error("Unable to login.")))})});g.write(c),g.end(),g.on("error",e=>{a(e)})}catch(e){u.default.error(e.message),a(e)}})}async refreshToken(e,n){return new Promise((o,i)=>{u.default.info("Refreshing token...");const a=s.stringify({refresh_token:e,client_id:f,grant_type:"refresh_token",scope:n}),c=r.request({host:"login.microsoftonline.com",path:`/${p}/oauth2/v2.0/token`,method:"POST",headers:{"Content-Type":"application/x-www-form-urlencoded","Content-Length":a.length}},e=>{const t=[];e.on("data",e=>{t.push(e)}),e.on("end",async()=>{if(200===e.statusCode){const e=this.getTokenFromResponse(t,n);this.setToken(e,n),u.default.info("Token refresh success"),o(e)}else u.default.error("Refreshing token failed"),i(new Error("Refreshing token failed."))})});c.write(a),c.end(),c.on("error",e=>{u.default.error(e.message),i(new Error(t.REFRESH_NETWORK_FAILURE))})})}clearSessionTimeout(e){const t=this._refreshTimeouts.get(e);t&&(clearTimeout(t),this._refreshTimeouts.delete(e))}removeInMemorySessionData(e){const t=this._tokens.findIndex(t=>t.sessionId===e);t>-1&&this._tokens.splice(t,1),this.clearSessionTimeout(e)}async handleTokenRefreshFailure(e,n,o,r,s){e.message===t.REFRESH_NETWORK_FAILURE?this.handleRefreshNetworkError(n,o,r):(await this.logout(n),s&&t.onDidChangeSessions.fire())}handleRefreshNetworkError(e,n,o,r=1){if(5===r)return void u.default.error("Token refresh failed after 5 attempts");1===r&&(this.removeInMemorySessionData(e),t.onDidChangeSessions.fire());const s=5*r*r;this.clearSessionTimeout(e),this._refreshTimeouts.set(e,setTimeout(async()=>{try{await this.refreshToken(n,o),t.onDidChangeSessions.fire()}catch(t){await this.handleRefreshNetworkError(e,n,o,r+1)}},1e3*s))}async logout(e){u.default.info(`Logging out of session '${e}'`),this.removeInMemorySessionData(e),0===this._tokens.length?await c.keychain.deleteToken():this.storeTokenData()}async clearSessions(){u.default.info("Logging out of all sessions"),this._tokens=[],await c.keychain.deleteToken(),this._refreshTimeouts.forEach(e=>{clearTimeout(e)}),this._refreshTimeouts.clear()}}},function(e,t){e.exports=require("crypto")},function(e,t){e.exports=require("https")},function(e,t){e.exports=require("querystring")},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});const o=n(8),r=n(9),s=n(10),i=n(11),a={number:"number",string:"string",undefined:"undefined",object:"object",function:"function"};function c(e){return typeof e===a.undefined}function u(e){return c(e)||null===e}function d(e){if(u(e))throw new Error("Assertion Failed: argument is undefined or null");return e}function l(e,t,n){s.readFile(t,(t,o)=>{t?(console.error(t),e.writeHead(404),e.end()):(e.writeHead(200,{"Content-Length":o.length,"Content-Type":n}),e.end(o))})}t.isUndefined=c,t.isUndefinedOrNull=u,t.assertIsDefined=d,t.createTerminateServer=function(e){const t={};let n=0;return e.on("connection",e=>{const o=n++;t[o]=e,e.on("close",()=>{delete t[o]})}),async()=>{const n=new Promise(t=>e.close(t));for(const e in t)t[e].destroy();return n}},t.startServer=async function(e){let t;function n(){clearTimeout(t)}const o=new Promise((n,o)=>{t=setTimeout(()=>{o(new Error("Timeout waiting for port"))},5e3),e.on("listening",()=>{const t=e.address();n("string"==typeof t?t:d(t).port.toString())}),e.on("error",e=>{o(new Error("Error listening to server"))}),e.on("close",()=>{o(new Error("Closed"))}),e.listen(0)});return o.then(n,n),o},t.createServer=function(e){let t;const n=new Promise((e,n)=>t={resolve:e,reject:n});let s;const a=new Promise((e,t)=>s={resolve:e,reject:t}),c=setTimeout(()=>{s.reject(new Error("Timeout waiting for code"))},3e5);function u(){clearTimeout(c)}const d=o.createServer(function(n,o){const a=r.parse(n.url,!0);switch(a.pathname){case"/signin":if((a.query.nonce||"").replace(/ /g,"+")===e)t.resolve({req:n,res:o});else{const e=new Error("Nonce does not match.");t.resolve({err:e,res:o})}break;case"/":l(o,i.join(__dirname,"../media/auth.html"),"text/html; charset=utf-8");break;case"/auth.css":l(o,i.join(__dirname,"../media/auth.css"),"text/css; charset=utf-8");break;case"/callback":s.resolve(async function(e,t){const n=t.query;if(!n||"string"==typeof n)throw new Error("No query received.");let o=n.error_description||n.error;o||((n.state||"").split(",")[1]||"").replace(/ /g,"+")!==e&&(o="Nonce does not match.");const r=n.code;if(!o&&r)return r;throw new Error(o||"No code received.")}(e,a).then(e=>({code:e,res:o}),e=>({err:e,res:o})));break;default:o.writeHead(404),o.end()}});return a.then(u,u),{server:d,redirectPromise:n,codePromise:a}}},function(e,t){e.exports=require("http")},function(e,t){e.exports=require("url")},function(e,t){e.exports=require("fs")},function(e,t){e.exports=require("path")},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});const o=n(0),r=n(1);const s=`${o.env.uriScheme}-vscode.login`,i="account";class a{constructor(){const e=function(){try{return n(13)}catch(e){console.log(e)}}();if(!e)throw new Error("System keychain unavailable");this.keytar=e}async setToken(e){try{return await this.keytar.setPassword(s,i,e)}catch(e){r.default.error(`Setting token failed: ${e}`)}}async getToken(){try{return await this.keytar.getPassword(s,i)}catch(e){return r.default.error(`Getting token failed: ${e}`),Promise.resolve(void 0)}}async deleteToken(){try{return await this.keytar.deletePassword(s,i)}catch(e){return r.default.error(`Deleting token failed: ${e}`),Promise.resolve(void 0)}}}t.Keychain=a,t.keychain=new a},function(e,t){e.exports=require("keytar")},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.toBase64UrlEncoding=function(e){return e.replace(/=/g,"").replace(/\+/g,"-").replace(/\//g,"_")}}]));
//# sourceMappingURL=https://ticino.blob.core.windows.net/sourcemaps/beaf391bc53136912e4f0bbdfb7844ad954247db/extensions/vscode-account/dist/extension.js.map