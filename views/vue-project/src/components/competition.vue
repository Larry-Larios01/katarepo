<script lang="ts">
import { ref , defineComponent, mergeProps} from 'vue'

export default defineComponent({

    name: 'competition',

    props: {
    players: {
      type: Number,
    },
    laps: {
        type: Number,
        default: 1000,
    },

  },
  
  setup() {
    
   



    // don't forget to expose the function as well.
    return {
 
    }
  }
})