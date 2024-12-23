<template>
    <div 
        v-if="alert.visible" 
        class="fixed top-4 right-4 bg-green-500 text-white p-4 rounded-md shadow-lg z-50">
        {{ alert.message }}
    </div>
    <button class="flex flex-col p-4 bg-violet-800 justify-between items-center text-white hover:bg-violet-950 rounded-md" @click="openModal = true">
        <CalendarDateRangeIcon class="justify-center size-8" aria-hidden="true" />
        <p>Appointments</p>
    </button>
    <div v-if="openModal" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
        <div class="bg-violet-200 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">
            <h2 class="text-xl font-bold mb-4 text-center">Schedule Appointments</h2>
            <form @submit.prevent="submitAppointment" class="flex flex-col gap-4">
                <h3 class="font-semibold text-primary-light text-center">Appointment Details</h3>
                <div class="flex flex-row gap-4 justify-between">
                    <div class="flex flex-col">
                        <label for="title" class="block text-sm text-left mb-2 font-medium">Title</label>
                        <input id="title" v-model="title" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required placeholder='David follow up'/>
                    </div>
                    <div class="flex flex-col">
                        <label for="date" class="block text-sm text-left mb-2 font-medium">Date</label>
                        <input id="date" v-model="date" type="date" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required/>
                    </div>
                    <div class="flex flex-col">
                        <label for="startTime" class="block text-sm text-left mb-2 font-medium">Start</label>
                        <input id="startTime" v-model="startTime" type="time" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required/>
                    </div>
                    <div class="flex flex-col">
                        <label for="endTime" class="block text-sm text-left mb-2 font-medium">End</label>
                        <input id="endTime" v-model="endTime" type="time" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required/>
                    </div>
                </div>
                <h3 class="font-semibold text-primary-light text-center">Patient Details</h3>
                <div class="flex flex-row gap-4 w-full">
                    <div class="flex flex-col w-full">
                        <label for="name" class="block text-sm text-left mb-2 font-medium">Name</label>
                        <input id="name" v-model="name" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required placeholder='Patient Name'/>
                    </div>
                    <div class="flex flex-col w-full">
                        <label for="mobile" class="block text-sm text-left mb-2 font-medium">Mobile</label>
                        <input id="mobile" v-model="mobile" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required placeholder='+254'/>
                    </div>
                </div>
                <div class="flex flex-row gap-4 w-full">
                    <div class="flex flex-col w-full">
                        <label for="location" class="block text-sm text-left mb-2 font-medium">Address</label>
                        <input id="location" v-model="location" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required placeholder='Kangemi'/>
                    </div>
                    <div class="flex flex-col w-full">
                        <label for="meetingType" class="block text-sm text-left mb-2 font-medium">Meeting Type</label>
                        <select v-model="meetingType" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required>
                            <option value="clinic">Clinic</option>
                            <option value="call">Phone Call</option>
                            <option value="other">Other</option>
                        </select>
                    </div>
                </div>
                <div v-if="meetingType === 'other'" class="flex flex-col w-full mt-4">
                    <label for="customLocation" class="block text-sm text-left mb-2 font-medium">Enter meet-up location</label>
                    <input id="customLocation" v-model="customLocation" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" placeholder="Enter custom meet-up location" />
                </div>
                <div class="flex justify-end gap-2">
                    <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">submit</button>  
                    <button @click="openModal = false" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">close</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
    import { CalendarDateRangeIcon } from '@heroicons/vue/20/solid';
    import { ref } from 'vue';

    const openModal = ref(false);
    const alert = ref({ visible: false, message: '' });

    const meetingType = ref('');
    const customLocation = ref('');
    const title = ref('');
    const date = ref('');
    const startTime = ref('');
    const endTime = ref('');
    const name = ref('');
    const mobile = ref('');
    const location = ref('');

    function showAlert(message) {
        alert.value = { visible: true, message };
        setTimeout(() => {
            alert.value.visible = false;
        }, 3000); // Alert disappears after 3 seconds
    }

    function submitAppointment () {
        if (title.value) {
            showAlert('Appointment submitted successfully!');
            openModal.value = false;
            reset();
        }
    }

    function reset () {
        meetingType.value = '';
        customLocation.value = '';
        title.value = '';
        date.value = '';
        startTime.value = '';
        endTime.value = '';
        name.value = '';
        mobile.value = '';
        location.value = '';
    }
</script>
