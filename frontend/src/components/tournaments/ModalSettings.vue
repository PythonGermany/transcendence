<script setup>
import { onMounted, ref, computed, defineProps } from 'vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle';
import router from '../../router';

const props = defineProps({
  message_child: {
    default: null
  },
  title_child: {
    default: null
  }
});

</script>

<template>
	<div class="modal fade" id="successModal" tabindex="-1" aria-labelledby="successModalLabel" aria-hidden="true">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="successModalLabel">{{ title_child }}</h5>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div class="modal-body">
					<p>{{ message_child }}</p>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
				</div>
			</div>
		</div>
	</div> 


</template>