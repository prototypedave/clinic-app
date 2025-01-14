<template>
    <div class="bg-violet-950 w-64 h-screen text-primary-light">
      <div class="flex place-items-center my-8 mx-6 gap-6">
        <img class="w-6 h-6 rounded-full" src="../assets/afyaLogo1.webp" />
        <h1 class="text-center font-bold text-lg"> Afya Bora Clinic </h1>
      </div>
      <div class="border mx-6 border-violet-800"></div>
      <div class='my-6 flex flex-col gap-4 mx-6 h-3/5'>
        <button class="p-2 flex justify-start items-center space-x-6 w-full focus:outline-none rounded focus:bg-purple-950 focus:text-white">
          <svg class="fill-stroke" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M9 4H5C4.44772 4 4 4.44772 4 5V9C4 9.55228 4.44772 10 5 10H9C9.55228 10 10 9.55228 10 9V5C10 4.44772 9.55228 4 9 4Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M19 4H15C14.4477 4 14 4.44772 14 5V9C14 9.55228 14.4477 10 15 10H19C19.5523 10 20 9.55228 20 9V5C20 4.44772 19.5523 4 19 4Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M9 14H5C4.44772 14 4 14.4477 4 15V19C4 19.5523 4.44772 20 5 20H9C9.55228 20 10 19.5523 10 19V15C10 14.4477 9.55228 14 9 14Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M19 14H15C14.4477 14 14 14.4477 14 15V19C14 19.5523 14.4477 20 15 20H19C19.5523 20 20 19.5523 20 19V15C20 14.4477 19.5523 14 19 14Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
          <p class="text-base leading-4">Dashboard</p>
        </button>
        <button class="p-2 flex justify-start items-center space-x-6 w-full focus:outline-none rounded focus:bg-purple-950 focus:text-white">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 20 20" fill="currentColor">
            <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z" />
          </svg>
          <p class="text-base leading-4">Employees</p>
        </button>
        <button class="p-2 flex justify-start items-center space-x-6 w-full focus:outline-none rounded focus:bg-purple-950 focus:text-white">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-5 w-5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 19.128a9.38 9.38 0 0 0 2.625.372 9.337 9.337 0 0 0 4.121-.952 4.125 4.125 0 0 0-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 0 1 8.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0 1 11.964-3.07M12 6.375a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0Zm8.25 2.25a2.625 2.625 0 1 1-5.25 0 2.625 2.625 0 0 1 5.25 0Z" />
          </svg>
          <p class="text-base leading-4">Patient</p>
        </button>
        <button class="p-2 flex justify-start items-center space-x-6 w-full focus:outline-none rounded focus:bg-purple-950 focus:text-white">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
            <path fill-rule="evenodd" d="M10.5 3.798v5.02a3 3 0 0 1-.879 2.121l-2.377 2.377a9.845 9.845 0 0 1 5.091 1.013 8.315 8.315 0 0 0 5.713.636l.285-.071-3.954-3.955a3 3 0 0 1-.879-2.121v-5.02a23.614 23.614 0 0 0-3 0Zm4.5.138a.75.75 0 0 0 .093-1.495A24.837 24.837 0 0 0 12 2.25a25.048 25.048 0 0 0-3.093.191A.75.75 0 0 0 9 3.936v4.882a1.5 1.5 0 0 1-.44 1.06l-6.293 6.294c-1.62 1.621-.903 4.475 1.471 4.88 2.686.46 5.447.698 8.262.698 2.816 0 5.576-.239 8.262-.697 2.373-.406 3.092-3.26 1.47-4.881L15.44 9.879A1.5 1.5 0 0 1 15 8.818V3.936Z" clip-rule="evenodd" />
          </svg>
          <p class="text-base leading-4">Lab</p>
        </button>
        <button class="p-2 flex justify-start items-center space-x-6 w-full focus:outline-none rounded focus:bg-purple-950 focus:text-white">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 20 20" fill="currentColor">
            <path d="M5 4a1 1 0 00-2 0v7.268a2 2 0 000 3.464V16a1 1 0 102 0v-1.268a2 2 0 000-3.464V4zM11 4a1 1 0 10-2 0v1.268a2 2 0 000 3.464V16a1 1 0 102 0V8.732a2 2 0 000-3.464V4zM16 3a1 1 0 011 1v7.268a2 2 0 010 3.464V16a1 1 0 11-2 0v-1.268a2 2 0 010-3.464V4a1 1 0 011-1z" />
          </svg>
          <p class="text-base leading-4">Records</p>
        </button>
      </div>
      <div class="border mx-6 border-violet-800"></div>
      <div class="flex place-items-center my-8 mx-6 gap-6">
        <img :src="user.image" class="w-10 h-10 mr-2 rounded-full" />
        <span className="flex-1 text-sm font-semibold ">{{ user.name }}</span>

        <UserProfile 
          
          :name="user.name"
          :role="user.role"/>
      </div>
    </div>
</template>

<script setup>
  import { useAuthStore } from '@/stores/auth';
  import UserProfile from '@/components/UserProfile.vue';
  import defaultProfileImage from '@/assets/male.png';

  const authStore = useAuthStore();
  const user = {
    image: authStore.getUser?.profile_image || defaultProfileImage,
    name: authStore.getUser?.name || "Guest",
    role: authStore.getRole || "guest"
  };
</script>