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
                <p class="text-primary-light text-center">Please fill in all the fields</p>
                <div class="flex flex-col gap-4 justify-between w-full">
                    <div class="flex flex-col">
                        <label for="title" class="block text-sm text-left mb-2 font-medium">Reason for Scheduling a meeting</label>
                        <input id="title" v-model="title" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required placeholder='David follow up'/>
                    </div>
                    <div class="flex flex-row gap-4 justify-between w-full">
                        <div class="flex flex-col w-full">
                            <label for="startTime" class="block text-sm text-left mb-2 font-medium">Meeting Date</label>
                            <input id="date" v-model="date" type="date" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required/>
                        </div>
                        <div class="flex flex-col w-full">
                            <label for="startTime" class="block text-sm text-left mb-2 font-medium">Start</label>
                            <input id="startTime" v-model="startTime" type="time" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required/>
                        </div>
                        <div class="flex flex-col w-full">
                            <label for="endTime" class="block text-sm text-left mb-2 font-medium">End</label>
                            <input id="endTime" v-model="endTime" type="time" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required/>
                        </div>
                    </div>
                    <div class="flex flex-row gap-4 justify-between w-full">
                        <div class="flex flex-col w-full">
                            <label for="first" class="block text-sm text-left mb-2 font-medium">First Name</label>
                            <input id="first" v-model="first" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required placeholder='Enter First Name'/>
                        </div>
                        <div class="flex flex-col w-full">
                            <label for="middle" class="block text-sm text-left mb-2 font-medium">Middle Name(optional)</label>
                            <input id="middle" v-model="middle" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" placeholder='Middle Name'/>
                        </div>
                        <div class="flex flex-col w-full">
                            <label for="last" class="block text-sm text-left mb-2 font-medium">Last Name</label>
                            <input id="last" v-model="last" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required placeholder='Enter Sir Name'/>
                        </div>
                    </div>
                    <div class="flex flex-row gap-4 justify-between w-full">
                        <div class="flex flex-col w-full">
                            <label for="mobile" class="block text-sm text-left mb-2 font-medium">Mobile</label>
                            <input id="mobile" v-model="mobile" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required placeholder='+254'/>
                        </div>
                        <div class="flex flex-col w-full">
                            <label for="email" class="block text-sm text-left mb-2 font-medium">Email</label>
                            <input id="email" v-model="email" type="email" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required placeholder='username@mail.com'/>
                        </div>
                        <div class="flex flex-col w-full">
                            <label for="reason" class="block text-sm text-left mb-2 font-medium ">Preferred Follow Up Method</label>
                            <select v-model="reason" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required>
                                <option value="mail">Email</option>
                                <option value="telephone">Phone Call</option>
                            </select>
                        </div>

                    </div>
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
    import { useAuthStore } from '@/stores/auth';
    import { useCalendarStore } from '@/stores/calendarStore';

    const openModal = ref(false);
    const alert = ref({ visible: false, message: '' });
    const today = new Date().toISOString().split('T')[0];

    const meetingType = ref('');
    const customLocation = ref('');
    const title = ref('');
    const startTime = ref('');
    const date = ref('');
    const endTime = ref('');
    const first = ref('');
    const middle = ref('');
    const last = ref('');
    const mobile = ref('');
    const email = ref('');
    const reason = ref('');

    const authStore = useAuthStore();
    const calendarStore = useCalendarStore();

    function showAlert(message) {
        alert.value = { visible: true, message };
        setTimeout(() => {
            alert.value.visible = false;
        }, 3000); 
    }

    async function submitAppointment () {
        if (title.value && startTime.value && endTime.value) {
            try {
                const response = await fetch("http://127.0.0.1:8000/appointments/add-appointment", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        'Authorization': `Bearer ${authStore.getAccessToken}`,
                    },
                    body: JSON.stringify({
                        title: title.value,
                        start: `${date.value} ${startTime.value}`,
                        end: `${date.value} ${endTime.value}`,
                        first: first.value,
                        middle: middle.value,
                        last: last.value,
                        mobile: mobile.value,
                        email: email.value,
                        reason: reason.value
                    })

                });
                if (!response.ok) {
                    const errorData = await response.json();
                    showAlert(errorData.error);
                }

                const success = await response.json();
                showAlert(success.message);
                openModal.value = false;
                reset();

                // update frontend with the save
                await calendarStore.getEvents(authStore.getAccessToken);

            } catch (error) {
                console.error(error);
                throw error; 
            }
        };
    }

    function reset () {
        meetingType.value = '';
        customLocation.value = '';
        title.value = '';
        startTime.value = '';
        endTime.value = '';
        first.value = '';
        middle.value = '';
        last.value = '';
        mobile.value = '';
        email.value = '';
        reason.value = '';
    }
</script>