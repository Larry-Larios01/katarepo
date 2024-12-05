<script lang="ts">
import { isTemplateExpression } from 'typescript';
import { ref , defineComponent} from 'vue'

export default defineComponent({

    name: 'Competition',

    props: {
    players: {
      type: Number
    },
    laps: {
        type: Number,
        default: 1000,
    },

  },
  
  setup() {


   const inputs = ref<String[]>([]);



   function submitValues()
   {
    console.log(inputs)

   }


   

   



    // don't forget to expose the function as well.
    return {
      inputs
 
    }
  }
});

</script>


<template>
  <div>
    <div v-for="(input, index) in inputs" :key="index">
      <label :for="'input-' + index">Input {{ index + 1 }}</label>
      <input
        type="text"
        v-model="inputs[index]"
        placeholder="Enter value"
      />
    </div>
    <button v-on:click="submitValues()>Submit</button>
  </div>
</template>





