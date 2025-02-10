<template>
    <div v-if="alert.visible" class="fixed top-4 right-4 bg-green-500 text-white p-4 rounded-md shadow-lg z-50">
        {{ alert.message }}
    </div>
	<div v-if="openMaternity" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      	<div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">        
        	<h2 class="text-xl font-bold mb-4 text-center"> Patient Maternity Care Form </h2>
        	<p class="text-center text-violet-500 mb-4"> Please fill in all the required fields * </p>
        	<form @submit.prevent="getMaternityData" class="flex flex-col gap-4">
          		<div class="flex justify-between gap-4">
          			<div class='w-full'>
                		<label for="edd" class="block text-sm text-left mb-2 font-medium">Estimated Due Date*</label>
                		<input v-model="edd" type="date" class="mt-1 pl-2 block w-full text-sm py-2 bg-violet-200 focus:border-violet-950 rounded-md shadow-sm" required />
              		</div>
            		<div class='w-full'>
                		<label for="gravidity" class="block text-sm text-left mb-2 font-medium ">Gravidity*</label>
                		<input v-model="gravidity" type="number" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required />
              		</div>
                    <div class='w-full'>
                        <label for="parity" class="block text-sm text-left mb-2 font-medium ">Parity*</label>
                        <input v-model="parity" type="number" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required />
                    </div>
            	</div>
            	<div class="flex justify-between gap-4">
              		<div class='w-full'>
	                	<label for="lmp" class="block text-sm text-left mb-2 font-medium ">Last Menstrual Period</label>
	                	<input v-model="lmp" type='date' class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required/>
              		</div>
              		<div class='w-full'>
                		<label for="place" class="block text-sm text-left mb-2 font-medium ">Preffered Place of Birth</label>
                		<input v-model="place" type='text' class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder="KNH" />
              		</div>
                    <div class='w-full'>
                        <label for="pain" class="block text-sm text-left mb-2 font-medium ">Pain Management Preference</label>
                        <input v-model="pain" type='text' class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder="natural child birth" />
                    </div>
            	</div>
                <div class="flex justify-between gap-4">
                    <div class='w-full'>
                        <label for="ppc" class="block text-sm text-left mb-2 font-medium ">Previous Pregnancy Complications</label>
                        <textarea v-model="ppc" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm "/>
                    </div>
                    <div class='w-full'>
                        <label for="pbc" class="block text-sm text-left mb-2 font-medium ">Previous Birth Complications</label>
                        <textarea v-model="pbc" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " />
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
    const openMaternity = computed(() => modalStore.getMaternity);

    const edd = ref('');
    const gravidity = ref('');
    const parity = ref('');
    const lmp = ref('');
    const ppc = ref('');
    const pbc = ref('');
    const place = ref('');
    const pain = ref('');

    const alert = ref({ visible: false, message: '' });
    const error = ref("");
    
    function showAlert(message) {
        alert.value = { visible: true, message };
        setTimeout(() => {
          alert.value.visible = false;
        }, 3000); 
    };

    async function getMaternityData () {
        const backend = "patient/maternity-record";

        if (edd.value && lmp.value) { 
            const body = JSON.stringify({
                "edd": edd.value,
                "gravidity": gravidity.value,
                "parity": parity.value,
                "lmp": lmp.value,
                "ppc": ppc.value,
                "pbc" : pbc.value,
                "place_of_birth" : place.value,
                "pain_management" : pain.value
                "id" : modalStore.getId,
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