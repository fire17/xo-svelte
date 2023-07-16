<script>
	// export let contenteditable = true;
	import { spring } from 'svelte/motion';
	// import { xo } from "./xo.js"
	// import { xo } from "./+page.svelte"
	import {  _datavar , _xo} from "./+page.js";
	console.log("#########@@@@@@@@@$$$$$$$$$$$$$$$$$$$$$$$",_datavar)
	// import {  _socket , _xo} from "./+page.js";
	// export let count = 111
	export let extraData;
	
	export let xo = _xo;
	// let xo = xox
	// let count = xo.count;
	// xo.count._value = 10
	// let count = xo.count._value;

	export let displayed_count = spring();
	$: displayed_count.set(xo.count._value);
	
	// $: displayed_count.set(count);
	// $: displayed_count.set(count);
	// $: displayed_count.set(count);
	$: offset = modulo($displayed_count, 1);

	function modulo(n, m) {
		// handle negative numbers
		return ((n % m) + m) % m;
	}
</script>


<!-- <input   -->
<!-- <h1>{_datavar}</h1> -->
<!-- <h1>{count}</h1> -->

<!-- <input bind:value={$displayed_count} 
	placeholder=100
	on:input={(v) => count = parseInt($displayed_count)}
	on:change={(v) => count = parseInt($displayed_count)} 		
	/> -->
	<!-- on:input={(v) => xo.count._value = parseInt($displayed_count)}
	on:change={(v) => xo.count._value = parseInt($displayed_count)} 		 -->

	<!-- on:change={() => displayed_count.set(parseInt(xo.count._value))}
		on:input={() => displayed_count.set(parseInt(xo.count._value))} -->
	<!-- <input bind:value={xo.count._value} 
	/> -->
	<!-- <input bind:value={count} 
	/> -->
	<!-- placeholder="Enter a message" -->
		<!-- on:change={() => change_count += 1}
		on:input={() => onChanges(xo.message._value)} 		 -->
<!-- <p>":::::::::" {xo.count._value}</p> -->
<!-- <p>":::::::::" {count}</p> -->
<div class="counter">
	<!-- <button contenteditable="true" bind:textContent={xo.count._value}  -->
	<!-- <button  
	on:click={() => (count = parseInt(count)-1)} aria-label="Decrease the counter by one">
		<svg aria-hidden="true" viewBox="0 0 1 1">
			<path d="M0,0.5 L1,0.5" />
		</svg>
	</button> -->
	<button  
	on:click={() => (xo.count._value = (parseInt(xo.count._value)-1||0))} aria-label="Decrease the counter by one">
		<svg aria-hidden="true" viewBox="0 0 1 1">
			<path d="M0,0.5 L1,0.5" />
		</svg>
	</button>

	<div class="counter-viewport">
		<div class="counter-digits" style="transform: translate(0, {100 * offset}%)">
			<strong class="hidden" aria-hidden="true">{Math.floor($displayed_count + 1)}</strong>
			<strong>{Math.floor($displayed_count)}</strong> 
			<!-- <strong>{$displayed_count.toFixed(2)}</strong>  -->
			
			<!-- <strong class="hidden" aria-hidden="true">{Math.floor($xo.count._value + 1)}</strong>
			<strong class="hidden" aria-hidden="true">{Math.floor(xo.count._value )}</strong>
		-->
			<!-- <strong>{Math.floor(xo.count._value)}</strong> -->
		</div>
	</div>

	<!-- <button on:click={() => (count = parseInt(count)+1)} aria-label="Increase the counter by one">
		<svg aria-hidden="true" viewBox="0 0 1 1">
			<path d="M0,0.5 L1,0.5 M0.5,0 L0.5,1" />
		</svg>
	</button> -->
	<button on:click={() => (xo.count._value = (parseInt(xo.count._value)+1||0))} aria-label="Increase the counter by one">
		<svg aria-hidden="true" viewBox="0 0 1 1">
			<path d="M0,0.5 L1,0.5 M0.5,0 L0.5,1" />
		</svg>
	</button>
</div>
	count: {xo.count._value} <nl></nl>
	precise:
	{$displayed_count}
	<div>
	<!-- <input bind:value={xo.count._value} /> 
	<input bind:value={$displayed_count} /> -->
	<!-- <input bind:value={xo.count._value} /> 
	<input bind:value={$displayed_count} /> -->
	<center>
		<h2 hidden=true>{extraData._value}</h2>
	</center>
	<br>
	
</div>
<style>
	.counter {
		display: flex;
		border-top: 1px solid rgba(0, 0, 0, 0.1);
		border-bottom: 1px solid rgba(0, 0, 0, 0.1);
		margin: 1rem 0;
	}

	.counter button {
		width: 2em;
		padding: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		border: 0;
		background-color: transparent;
		touch-action: manipulation;
		font-size: 2rem;
	}

	.counter button:hover {
		background-color: var(--color-bg-1);
	}

	svg {
		width: 25%;
		height: 25%;
	}

	path {
		vector-effect: non-scaling-stroke;
		stroke-width: 2px;
		stroke: #444;
	}

	.counter-viewport {
		width: 8em;
		height: 4em;
		overflow: hidden;
		text-align: center;
		position: relative;
	}

	.counter-viewport strong {
		position: absolute;
		display: flex;
		width: 100%;
		height: 100%;
		font-weight: 400;
		color: var(--color-theme-1);
		font-size: 4rem;
		align-items: center;
		justify-content: center;
	}

	.counter-digits {
		position: absolute;
		width: 100%;
		height: 100%;
	}

	.hidden {
		top: -100%;
		user-select: none;
	}
</style>
