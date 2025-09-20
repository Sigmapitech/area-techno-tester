<script setup lang="ts">
import HelloWorld from './HelloWorld.vue'
import { ref } from 'vue'
import { Background } from '@vue-flow/background'
import { Controls } from '@vue-flow/controls'
import { VueFlow, useVueFlow, type Node, type Edge } from '@vue-flow/core'
import CustomNode from './CustomNode.vue'
import CustomEdge from './CustomEdge.vue'

const { onConnect, addEdges } = useVueFlow()

const nodes = ref<Node[]>([
  { id: '1', type: 'input', label: 'Node 1', position: { x: 250, y: 5 } },
  { id: '2', type: 'output', label: 'Node 2', position: { x: 100, y: 100 } },
  { id: '3', type: 'custom', label: 'Node 3', position: { x: 400, y: 100 } },
])

const edges = ref<Edge[]>([
  { id: 'e1-2', source: '1', target: '2', type: 'custom' },
  { id: 'e1-3', source: '1', target: '3', animated: true },
])

onConnect((params) => {
  addEdges([params])
})

</script>

<template>
  <VueFlow
    v-model:nodes="nodes"
    v-model:edges="edges"
    fit-view-on-init
    class="vue-flow-basic-example"
    :default-zoom="1.5"
    :min-zoom="0.2"
    :max-zoom="4"
    style="height: 60vh;"
  >
    <Background pattern-color="#aaa" :gap="8" />

    <Controls />

    <template #node-custom="nodeProps">
      <CustomNode v-bind="nodeProps" />
    </template>

    <template #edge-custom="edgeProps">
      <CustomEdge v-bind="edgeProps" />
    </template>
  </VueFlow>

  <div style="background-color: black;">
    <div>
      <a href="https://vite.dev" target="_blank">
        <img src="/vite.svg" class="logo" alt="Vite logo" />
      </a>
      <a href="https://vuejs.org/" target="_blank">
        <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
      </a>
    </div>

    <HelloWorld msg="Vite + Vue" />
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
