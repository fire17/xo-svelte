<script>
	import Counter from './Counter.svelte';
	import welcome from '$lib/images/svelte-welcome.webp';
	import welcome_fallback from '$lib/images/svelte-welcome.png';
	// import * as xox from './xo.js'
	// import { _exp } from "./xo";
	// import { _exp } from "./xo";
	// import {  _socket , _xo} from "./+page.js";
	import {  _datavar, _socket , _xo} from "./+page.js";
	let xo = _xo
	let socket = _socket
	import { change_count, input_count } from './vars';
	// import {static_props} from './vars.js';
	if (xo.run_once._value == "ok"){
		// alert("started")

	}
	else{
		xo.count = 101
		xo.message2 = '-------------';
		// for ( let key in static_props){
		// 	xo[key] = static_props[key]
		// }
		xo.run_once = "ok"
		xo.message = "~dynamic message~"
		xo.change_count._value = change_count;
		xo.input_count._value = input_count;

		// alert("init")
	}
	// xo.count = 10
	// export let xo = xo
	// export let xo = _exp("svelte", "Awesome!");

	// $: xo = _exp("SVELTE", "Awesome!")
	console.log(xo);
	// $: message = "xdynamic messages"
	// $: message = xo.message._value












	// import io from 'socket.io-client';
	//   import { Server } from 'socket.io';
	let name = "xo-svelte";



  socket.on('server_update', msg => {
		console.log("::::::::::::::::::::::::::::: new message: ", msg)
		xo.message2 = msg.data._value;
		// Counter
		// xo.message = msg.data
		// alert (msg.message)
		xo.message = "X"+msg.message
		function nested_update(obj, ref, name){
			for (var prop in obj) {
				if (prop == "_value"){
					// alert("SET "+ref._name+"["+prop+ ":"+obj[prop]);
					// ref.set(obj[prop])
					ref[prop] = obj[prop]
					// alert("Key:" +name +" " + prop+ " Value "+obj[prop]);
				}
				if (typeof obj[prop] === 'object'){
					// alert("Key:" + prop+ " is Nested ");
					// nested_update(obj[prop], ref[prop], prop);
					nested_update(obj[prop], ref[prop], prop);
				}
				else{
					// alert("SET "+ref._name+"["+prop+ ":"+obj[prop]);
					ref[prop] = obj[prop]
				}
				// alert("Value:" + msg[prop]);
				// ref[prop] = msg[prop];
			}
			// alert("done",name)
		}
		// alert("type:" + typeof(msg));
		// alert("type:" + Object.getOwnPropertyNames(msg));
		// alert("type:" + Object.keys(msg));
		
		// for (var prop in msg) {
		// alert("Key:" + prop+ " type "+typeof(msg[prop]));
		// // alert("Value:" + msg[prop]);
		// xo[prop] = msg[prop];
		// }
		nested_update(msg, xo, "root")
		
    });
// socketIoHandler.js

export function onChanges(msg) {
	xo.input_count._value = xo.input_count._value + 1
	// _datavar = msg
	console.log(":::::::::::::::::::::::::::::")
	socket.emit('user_msg', msg);
	console.log(":::::::::::::::::::::::::::::")
}
export function sendSocketIOMessage(msg) {
	console.log(":::::::::::::::::::::::::::::")
	socket.emit('user_msg', msg);
	console.log(":::::::::::::::::::::::::::::")
}
// export function injectSocketIO(server) {
	
//     socket.on('new message', msg => {
// 		console.log("::::::::::::::::::::::::::::: new message, msg: ", msg)
// 		message = msg;
//     });
	
	// const io = new Server(server);
    // io.on('connection', (socket) => {
    //     let username = `User ${Math.round(Math.random() * 999999)}`;
    //     socket.emit('name', username);

    //     socket.on('message', (message) => {
    //         io.emit('message', {
    //             from: username,
    //             message: message,
    //             time: new Date().toLocaleString()
    //         });
    //     });
    // });

//     console.log('SocketIO injected');
// }
//   onMount(async () => {
//     socket = io('http://127.0.0.1:5000');

//     socket.on('new message', msg => {
//       message = msg;
//     });
//   });



	import Grid from "svelte-grid";
	import gridHelp from "svelte-grid/build/helper/index.mjs";
// import Grid from "../../components/svelte-grid/index.svelte";
// import gridHelp from "../../components/svelte-grid/utils/helper.js";
// import { openSource } from "./github.js";

const COLS = 6;

const id = () => "_" + Math.random().toString(36).substr(2, 9);

const randomNumberInRange = (min, max) => Math.random() * (max - min) + min;

let items = [
  {
    [COLS]: gridHelp.item({
      x: 0,
      y: 0,
      w: 2,
      h: 2,
    }),
    id: id(),
  },

  {
    [COLS]: gridHelp.item({
      x: 2,
      y: 0,
      w: 2,
      h: 2,
    }),
    id: id(),
  },
];

const cols = [[1100, 6]];

function add() {
  let newItem = {
    6: gridHelp.item({
      w: Math.round(randomNumberInRange(1, 4)),
      h: Math.round(randomNumberInRange(1, 4)),
      x: 0,
      y: 0,
    }),
    id: id(),
  };

  let findOutPosition = gridHelp.findSpace(newItem, items, COLS);

  newItem = {
    ...newItem,
    [COLS]: {
      ...newItem[COLS],
      ...findOutPosition,
    },
  };

  items = [...items, ...[newItem]];
}

const addAt = () => {
  let newItem = {
    6: gridHelp.item({
      w: Math.round(randomNumberInRange(1, 4)),
      h: Math.round(randomNumberInRange(1, 4)),
      x: 0,
      y: 0,
    }),
    id: id(),
  };

  items = [...[newItem], ...items];

  items = gridHelp.adjust(items, COLS);
};

const remove = (item) => {
  items = items.filter((value) => value.id !== item.id);

  if (adjustAfterRemove) {
    items = gridHelp.adjust(items, COLS);
  }
};

let adjustAfterRemove = false;
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>







<button on:click={add}>Add (random size)</button>
<button on:click={addAt}>Add random (x=0,y=0)</button>
<label>
  <input type="checkbox" bind:checked={adjustAfterRemove} />
  Adjust elements after removing an item
</label>

<div class=demo-container>
  <Grid bind:items={items} rowHeight={100} let:item let:dataItem {cols}>
    <div class=demo-widget>
      <span on:pointerdown={e => e.stopPropagation()}
        on:click={() => remove(dataItem)}
        class=remove
        >
        ✕
      </span>
      <p>{dataItem.id}</p>
    </div>
  </Grid>
</div>










	<!-- <Grid {cols} bind:items={items} let:item={item}>
	  <div>{item.id}</div>
</Grid> -->
	
<!-- <Grid gap={[10, 5]} {items} {cols} rowHeight={150} let:item let:dataItem>
  <div>{item.data}</div>
</Grid> -->





<h1>
		<!-- <span class="welcome">
			<picture>
				<source srcset={welcome} type="image/webp" />
				<img src={welcome_fallback} alt="Welcome" />
			</picture>
		</span> -->

		Welcome! to your new<br />XO-Svelte app
	</h1>
<!-- 
	<h2>
		try editing <strong>src/routes/+page.svelte</strong>
	</h2> -->
	
	<!-- <Counter bind:count={xo.count._value} newh={message}  /> -->
	<Counter bind:xo={xo} extraData={xo.message2}  />



	<!-- <Counter bind:newcount={message} $displayed_count={xo.count._value} /> -->
	<!-- <Counter bind:newcount={placeholder} newh={message}  /> -->
	<!-- {xo.message} -->
	<!-- {message} -->
	<!-- <h1>Hello {_datavar}!</h1> -->
	<div>

		Edit Counter  : <input bind:value={xo.count._value}  
		on:input={() => xo.count._value = (isNaN(parseInt(xo.count._value)) ? 0 : parseInt(xo.count._value))}
	/>
	</div>

	<div>
			<input bind:value={xo.message._value} 
			placeholder="Enter a message XXX"
			on:change={() => xo.change_count._value = xo.change_count._value+1}
			on:input={() => onChanges(xo.message._value)} 		
			/>

			<button on:click={() => sendSocketIOMessage(xo.message._value)}>
				Send message
			</button>
		</div>
		
	<!-- <input bind:value={message} placeholder="Enter a message" on:change={() => change_count += 1}
	on:input={() => onChanges(message)} />
		<button on:click={() => sendSocketIOMessage(message)}>
			Send message
		</button> -->
			
		<p>
			Sub-message:       {xo.message2._value}
		</p>
		{xo.data.extra._value}
		| Change Count: {xo.change_count._value}
		| Input Count: {xo.input_count._value}
		
</section>


<style>
	.remove { cursor: pointer; position: absolute; right: 5px; top: 3px; }

	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}
	/* For welcome image */
/* 
	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	} */
</style>
