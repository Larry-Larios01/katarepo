<script lang="ts">
import { ref , defineComponent} from 'vue'

export default defineComponent({

    name: 'Competition',

    props: {
    players: {
      type: Number,
      default:5
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
    alert(inputs.value)

   }


   

   



    // don't forget to expose the function as well.
    return {
      inputs,
      submitValues
 
    }
  }
});

</script>


<template>
  <div>
    <div v-for="n in players">
      {{ n }}
      <input
        type="text"
        v-model="inputs[n-1]"
        placeholder="Enter value"
      />
    </div>
    <button v-on:click="submitValues()">Submit</button>
  </div>
</template>





