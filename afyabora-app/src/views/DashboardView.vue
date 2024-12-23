<!-- src/views/HomeView.vue -->
<template>
  <div class="flex flex-row text-white max-h-screen">
    <SideBar />
    <div class="flex-1 mx-auto max-w-7xl">
      <AdminHeader />
      <div class="flex m-4">
        <div class="flex-1 grid grid-cols-3 gap-4 max-h-48 text-base">
          <Appointments />
          <Appointments />
          <Appointments />
          <Appointments />
          <Appointments />
          <Appointments />
          <Appointments />
          <Appointments />
        </div>
        <div class="flex-1 ml-8">
          <AppointmentCalender />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AdminHeader from '@/components/AdminHeader.vue';
import SideBar from '@/components/SideBar.vue';
import AppointmentCalender from '@/components/AppointmentCalender.vue';
import Appointments from '@/components/modals/AppointmentModal.vue';

export default {
  components: {
    AdminHeader,
    SideBar,
    AppointmentCalender,
    Appointments,
  }
}
</script>
