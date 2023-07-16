// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
export const prerender = true;
export let _datavar = "Svelte"

import io from 'socket.io-client';
export let _socket = io('http://127.0.0.1:5000');
import { _exp } from './xo'
export let _xo  = _exp("svelte", "Awesome!")


// class expando{
//   get(target, name) {
//     return `Value for attribute ${target} ${name}`
//   }
// }

// export function _exp(_name = "", _value=null, _parent = null){
//   	let payload = {"_name":_name}
//   	if (_value != null){
//       payload["_value"]=_value
//     }
// 	let x = new Proxy({"_name":_name,"_parent":_parent, "_value":_value}, handler);
// 	//x._name = name;
// 	return x
// }
// let handler = {
//   apply(target, name, data){
//     return target._name+"/"+name+"!!!!!!!!!!!!!!!!!!!!!!!"
//     console.log("@@@@@@@@@@@@@@",target,name,data)
//     target[name] = data
//      console.log("@@@ apply",target)

//     return target
    
//   },
//   set(target, name, data){
//     console.log("!!!@",target,name,data)
//     let spc = {"_value":1,"_name":1,"toJSON":1,"nodeType":1,"id":1,"className":1
//                  ,"nodeName":1,"parentNode":1,"currentStyle":1,"outerHTML":1, 
//                 "window":1,"length":1}
//     if (name in spc)
//     {
//       return Reflect.set(target, name, data)
//     }
//     else
//     {
//       	if (name in target){
//         	target[name]._value = data
//         	return target[name]._value
//            return target[name]
//            return Reflect.set(target, name, data)
//         }
//         else
//         {
//     		// target[name] = exp(target._name+"/"+name,data, _parent = target)
//     		target[name] = _exp(target._name+"/"+name,data, target)
//         	return target[name]._value
//         }    
//     }
   
//      console.log("@@@ set",target)

//     return target[name]
    
//   },
//   get(target, name, reciever) {
    
//     if (typeof target[name] === 'function') {
//       //return target[name].bind(target);
//       return target[name];

//     }

    
//     if (name in target){
//       if (target[name] != null && typeof target[name]._value === 'function') {
//         //return target[name]._value.bind(target);
//         //return target[name]._value;

//       }
//       return target[name]
//     }
    
//     //return Reflect.get(...arguments);
//     // console.log("..........2....",name)
//     let spc = {"_value":1,"_name":1,"toJSON":1,"nodeType":1,"id":1,"className":1
//                ,"nodeName":1,"parentNode":1,"currentStyle":1,"outerHTML":1, 
//               "window":1,"length":1}
//     if (name in spc)
//     {
//        return Reflect.get(target, name, reciever)
//     }
//     else{ 
//       // target[name] = exp(target._name+"/"+name,null,parent=target)
//       target[name] = _exp(target._name+"/"+name,null,target)
//         }
  
    
//     return target[name]
//     return `Value for attribute ${target} ${name}`
//   },
  
// }


// let xo = exp("namespace", "Awesome!")
// export const _xo = exp("namespace", "Awesome!")
// import { xo } from "./xo";

// import { xo } from "./+page.svelte";

// let xo = _exp("svelte", "Awesome!")
// // export let xo = exp("svelte", "Awesome!");

// console.log('.......')
// // let x = new Proxy({}, expando);
// console.log(xo); // produces message: "Value of attribute 'lskdjoau'"

// // // console.log(x.lskdjoau); // produces message: "Value of attribute 'lskdjoau'"
// xo.a = 3
// xo.a.b.c.d.e.f.g.h = 3
// xo.a.b.c.d.e = () => {return "EEEEEEEEEEEEEEEEEEE"}
// xo.a.b.c = () => {return "CCCCCCCCCCCCC"}


// console.log(xo); // produces message: "Value of attribute 'lskdjoau'"
// console.log(xo._name); // produces message: "Value of attribute 'lskdjoau'"
// console.log(xo.a.b.c._value()); // produces message: "Value of attribute 'lskdjoau'"
// console.log(xo.a.b.c.d.e._value()); // produces message: "Value of attribute 'lskdjoau'"
// console.log(xo.a.b.c.d.e.f.g.h._value); // produces message: "Value of attribute 'lskdjoau'"
// // console.log(xo.a.b.c.d.e.f.g.h); // produces message: "Value of attribute 'lskdjoau'"
// // export let _xo=xo