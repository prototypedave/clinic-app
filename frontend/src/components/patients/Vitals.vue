<template>
    <div v-if="alert.visible" class="fixed top-4 right-4 bg-green-500 text-white p-4 rounded-md shadow-lg z-50">
        {{ alert.message }}
    </div>
	<div v-if="openVitalSigns" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      	<div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">        
        	<h2 class="text-xl font-bold mb-4 text-center"> Vital Tests Form </h2>
        	<form @submit.prevent="getVitalSigns" class="flex flex-col gap-4">
                <div class='flex gap-4'>
          			<div class='w-full'>
                		<label for="temp" class="block text-sm text-left mb-2 font-medium">Temperature*</label>
                		<input v-model="temp" type="number" class="mt-1 pl-2 block w-full text-sm py-2 bg-violet-200 focus:border-violet-950 rounded-md shadow-sm" required placeholder="37" />
                  	</div>
            		<div class='w-full'>
                		<label for="pulse" class="block text-sm text-left mb-2 font-medium ">Pulse</label>
                		<input v-model="pulse" type="number" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm "/>
                  	</div>
                </div>
                <div class="flex gap-4">
                    <div class='w-full'>
                        <label for="bp" class="block text-sm text-left mb-2 font-medium ">Blood Pressure</label>
                        <input v-model="bp" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm" />
                    </div>
                    <div class='w-full'>
                        <label for="rr" class="block text-sm text-left mb-2 font-medium ">Respiratory Rate</label>
                        <input v-model="rr" type="number" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm" />
                    </div>
                </div>
                <div class='flex gap-4'>
                    <div class='w-full'>
                        <label for="weight" class="block text-sm text-left mb-2 font-medium ">Weight</label>
                        <input v-model="weight" type="number" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm"/>
                    </div>
                    <div class='w-full'>
                        <label for="height" class="block text-sm text-left mb-2 font-medium ">Height</label>
                        <input v-model="bp" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm"/>
                    </div>
                </div>
	            <div class="flex justify-end gap-4 h-10">
		            <button @click="openModal = true; openPatientInfo = false" type="button" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md focus:ring focus:ring-secondary-btn-fcs">back</button>
		            <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
		        </div>
        	</form>
      	</div>
    </div>
</template>

<script setup>
	import { ref } from 'vue';
    import { useAuthStore } from '@/stores/auth';
    import { usePatientModalStore } from '@/stores/patientModal';
    import { computed } from 'vue';

    const authStore = useAuthStore();
    const modalStore = usePatientModalStore();
    const openVitalSigns = computed(() => modalStore.getVitals);

    const temp = ref('');
    const pulse = ref('');
    const bp = ref('');
    const rr = ref('');
    const weight = ref('');
    const height = ref('');

    const alert = ref({ visible: false, message: '' });
    const error = ref("");
    
    function showAlert(message) {
        alert.value = { visible: true, message };
        setTimeout(() => {
          alert.value.visible = false;
        }, 3000); 
    };

    async function getRehabData () {
        const backend = "patient/vitals-record";

        if (temp.value) { 
            const body = JSON.stringify({
                "temperature": temp.value,
                "pulse": pulse.value,
                "blood_pressure": bp.value,
                "respiratory_rate" : rr.getId,
                "weight": weight.value,
                "height": height.value,
                "id" : modalStore.getId
            });

            // poll backend
            const msg = await authStore.APICall({ body: body, api: backend });
            if (msg.success) {
                showAlert(msg.data.message);
                setTimeout(() => {
                    modalStore.reset();
                    //modalStore.prenatalTestModal();
                }, 3000 );              
            } else {
                showAlert(msg.data.error);
            }
        }
    }

</script>