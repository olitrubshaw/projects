const stopSchedules = {
    "Clement Street": [
        { service: "126", times: "05:34, 10:18, 15:17, 20:17" },
        { service: "126", times: "06:05, 10:38, 15:37, 20:47" },
        { service: "126", times: "06:25, 10:58, 15:57, 21:17" },
        { service: "126", times: "06:43, 11:17, 16:17, 21:47" },
        { service: "126", times: "07:00, 11:37, 16:37, 22:17" },
        { service: "126", times: "07:19, 11:57, 16:57, 22:47" },
        { service: "126", times: "07:40, 12:17, 17:17, 23:17" },
        { service: "126", times: "07:59, 12:37, 17:37, 23:50" },
        { service: "126", times: "08:19, 12:57, 17:57, --:--" },
        { service: "126", times: "08:41, 13:17, 18:17, --:--" },
        { service: "126", times: "09:02, 13:37, 18:47, --:--" },
        { service: "126", times: "09:22, 13:57, 19:17, --:--" },
        { service: "126", times: "09:38, 14:17, 19:47, --:--" },
        { service: "126", times: "09:56, 14:37, --:--, --:--" }
    ],
    "Icknield Port Road": [
        { service: "8A", times: "04:59, 09:22, 13:25, 17:26" },
        { service: "8A", times: "05:29, 09:35, 13:38, 17:41" },
        { service: "8A", times: "05:59, 09:49, 13:48, 17:53" },
        { service: "8A", times: "06:17, 10:02, 14:01, 18:04" },
        { service: "8A", times: "06:36, 10:15, 14:15, 18:16" },
        { service: "8A", times: "06:48, 10:28, 14:26, 18:30" },
        { service: "8A", times: "07:01, 10:40, 14:39, 18:43" },
        { service: "8A", times: "07:12, 10:53, 14:51, 18:57" },
        { service: "8A", times: "07:25, 11:06, 15:00, 19:15" },
        { service: "8A", times: "07:34, 11:19, 15:12, 19:36" },
        { service: "8A", times: "07:45, 11:32, 15:26, 19:56" },
        { service: "8A", times: "07:57, 11:44, 15:39, 20:19" },
        { service: "8A", times: "08:12, 11:57, 15:52, 20:40" },
        { service: "8A", times: "08:27, 12:10, 16:06, 21:10" },
        { service: "8A", times: "08:42, 12:23, 16:18, 21:40" },
        { service: "8A", times: "08:56, 12:35, 16:33, 22:10" },
        { service: "8A", times: "09:08, 12:47, 16:47, 22:40" },
        { service: "8A", times: "09:22, 12:59, 17:01, 23:10" },
        { service: "8A", times: "09:35, 13:35, 17:42, --:--" },
    ],
    "Ladywood Fire Station": [
        { service: "80", times: "05:55, 09:01, 12:32, 14:29" },
        { service: "80", times: "06:26, 09:11, 12:44, 14:41" },
        { service: "80", times: "06:59, 09:22, 12:55, 14:53" },
        { service: "80", times: "07:14, 09:32, 13:06, 15:05" },
        { service: "80", times: "07:29, 09:42, 13:17, 15:17" },
        { service: "80", times: "07:42, 09:52, 13:29, 15:29" },
        { service: "80", times: "07:59, 10:01, 13:41, 15:41" },
        { service: "80", times: "08:10, 10:10, 13:53, 15:53" },
        { service: "80", times: "08:20, 10:19, 14:05, 16:05" },
        { service: "80", times: "08:32, 10:28, 14:17, 16:17" },
        { service: "80", times: "08:42, 10:37, 14:29, --:--" },
        { service: "80", times: "08:52, 10:46, --:--, --:--" }
    ],
    "Leyburn Road": [
        {service: "8A", times: "05:01, 09:25, 13:27, 17:28"},
        {service: "8A", times: "05:31, 09:38, 13:40, 17:43"},
        {service: "8A", times: "06:01, 09:51, 13:50, 17:55"},
        {service: "8A", times: "06:19, 10:04, 14:03, 18:07"},
        {service: "8A", times: "06:37, 10:17, 14:17, 18:18"},
        {service: "8A", times: "06:49, 10:30, 14:28, 18:32"},
        {service: "8A", times: "07:02, 10:42, 14:41, 18:45"},
        {service: "8A", times: "07:14, 10:55, 14:53, 18:59"},
        {service: "8A", times: "07:27, 11:08, 15:03, 19:16"},
        {service: "8A", times: "07:36, 11:21, 15:15, 19:37"},
        {service: "8A", times: "07:47, 11:34, 15:28, 19:57"},
        {service: "8A", times: "08:00, 11:46, 15:41, 20:20"},
        {service: "8A", times: "08:14, 11:59, 15:54, 20:42"},
        {service: "8A", times: "08:29, 12:12, 16:08, 21:12"},
        {service: "8A", times: "08:44, 12:25, 16:20, 21:42"},
        {service: "8A", times: "08:58, 12:37, 16:35, 22:12"},
        {service: "8A", times: "09:11, 12:49, 16:49, 22:42"},
        {service: "8A", times: "09:25, 13:01, 17:03, 23:12"},
        {service: "8A", times: "—-:--, —-:--, —-:--, 23:42"}
    ],
    "Osler Street": [
        {service: "80", times: "12:18, 13:16, 14:04, 15:17"},
        {service: "80", times: "12:30, 13:28, 14:16, 15:29"},
        {service: "80", times: "12:42, 13:40, 14:28, 15:41"},
        {service: "80", times: "12:53, 13:52, 14:40, 15:53"},
        {service: "80", times: "13:05, 14:04, 14:52, 16:05"}
    ],
    "Cope Street": [
        {service: "8A", times: "05:27, 09:36, 13:40, 17:39"},
        {service: "8A", times: "05:52, 10:00, 14:00, 18:00"},
        {service: "8A", times: "06:09, 10:20, 14:19, 18:24"},
        {service: "8A", times: "06:23, 10:38, 14:40, 18:50"},
        {service: "8A", times: "06:38, 10:59, 15:00, 19:18"},
        {service: "8A", times: "06:51, 11:18, 15:15, 19:39"},
        {service: "8A", times: "07:02, 11:38, 15:28, 19:59"},
        {service: "8A", times: "07:13, 11:56, 15:49, 20:21"},
        {service: "8A", times: "07:24, 12:17, 16:01, 20:43"},
        {service: "8A", times: "07:37, 12:36, 16:20, 21:04"},
        {service: "8A", times: "07:56, 12:55, 16:40, 21:34"},
        {service: "8A", times: "08:13, 13:15, 16:58, 22:04"},
        {service: "8A", times: "08:35, 13:28, 17:14, 22:34"},
        {service: "8A", times: "08:55, 13:47, 17:26, 23:04"},
        {service: "8A", times: "09:15, 13:53, 17:50, 23:34"},
    ],
    "Ruston Street": [
        {service: "8A", times: "05:03, 09:27, 13:29, 17:30"},
        {service: "8A", times: "05:33, 09:40, 13:42, 17:45"},
        {service: "8A", times: "06:03, 09:53, 13:52, 17:57"},
        {service: "8A", times: "06:21, 10:06, 14:05, 18:09"},
        {service: "8A", times: "06:39, 10:19, 14:19, 18:20"},
        {service: "8A", times: "06:51, 10:32, 14:30, 18:34"},
        {service: "8A", times: "07:04, 10:44, 14:43, 18:47"},
        {service: "8A", times: "07:16, 10:57, 14:55, 19:01"},
        {service: "8A", times: "07:29, 11:10, 15:05, 19:18"},
        {service: "8A", times: "07:38, 11:23, 15:17, 19:39"},
        {service: "8A", times: "07:49, 11:36, 15:30, 19:59"},
        {service: "8A", times: "08:02, 11:48, 15:43, 20:22"},
        {service: "8A", times: "08:16, 12:01, 15:56, 20:44"},
        {service: "8A", times: "08:31, 12:14, 16:10, 21:14"},
        {service: "8A", times: "08:46, 12:27, 16:22, 21:44"},
        {service: "8A", times: "09:00, 12:39, 16:37, 22:14"},
        {service: "8A", times: "09:13, 12:51, 16:51, 22:44"},
        {service: "8A", times: "09:27, 13:03, 17:05, 23:14"},
        {service: "8A", times: "—-:--, —-:--, —-:--, 23:44"}
    ],
    "Crescent Theatre": [
        {service: "8A", times: "05:48, 09:58, 14:00, 18:09"},
        {service: "8A", times: "06:18, 10:11, 14:13, 18:29"},
        {service: "8A", times: "06:38, 10:24, 14:26, 18:49"},
        {service: "8A", times: "06:47, 10:37, 14:39, 19:09"},
        {service: "8A", times: "06:55, 10:49, 14:52, 19:29"},
        {service: "8A", times: "07:05, 11:01, 15:05, 19:49"},
        {service: "8A", times: "07:13, 11:14, 15:18, 20:09"},
        {service: "8A", times: "07:24, 11:27, 15:31, 20:38"},
        {service: "8A", times: "07:35, 11:39, 15:44, 21:08"},
        {service: "8A", times: "07:46, 11:51, 15:57, 21:38"},
        {service: "8A", times: "07:59, 12:04, 16:10, 22:08"},
        {service: "8A", times: "08:13, 12:17, 16:23, 22:38"},
        {service: "8A", times: "08:27, 12:30, 16:36, 23:08"},
        {service: "8A", times: "08:41, 12:43, 16:49, 23:38"},
        {service: "8A", times: "08:56, 12:56, 17:02"},
        {service: "8A", times: "09:10, 13:09, 17:15"},
        {service: "8A", times: "09:22, 13:22, 17:28"},
        {service: "8A", times: "09:35, 13:35, 17:42"},
    ],
    "King Edwards Road": [
        {service: "8A", times: "05:08, 09:32, 13:34, 17:35"},
        {service: "8A", times: "05:38, 09:45, 13:47, 17:50"},
        {service: "8A", times: "06:08, 09:58, 13:57, 18:02"},
        {service: "8A", times: "06:26, 10:11, 14:10, 18:14"},
        {service: "8A", times: "06:44, 10:24, 14:24, 18:25"},
        {service: "8A", times: "06:56, 10:37, 14:35, 18:39"},
        {service: "8A", times: "07:09, 10:49, 14:48, 18:52"},
        {service: "8A", times: "07:21, 11:02, 15:00, 19:06"},
        {service: "8A", times: "07:34, 11:15, 15:10, 19:23"},
        {service: "8A", times: "07:43, 11:28, 15:22, 19:44"},
        {service: "8A", times: "07:54, 11:41, 15:35, 20:04"},
        {service: "8A", times: "08:07, 11:53, 15:48, 20:27"},
        {service: "8A", times: "08:21, 12:06, 16:01, 20:49"},
        {service: "8A", times: "08:36, 12:19, 16:15, 21:19"},
        {service: "8A", times: "08:51, 12:32, 16:27, 21:49"},
        {service: "8A", times: "09:05, 12:44, 16:42, 22:19"},
        {service: "8A", times: "09:18, 12:56, 16:56, 22:49"},
        {service: "8A", times: "09:32, 13:08, 17:10, 23:19"},
        {service: "8A", times: "—-:--, —-:--, —-:--, 23:49"}
    ],
    "Spring Hill Island": [
        {service: "82 & 87", times: "05:03, 09:41, 14:09, 18:24"},
        {service: "82 & 87", times: "05:25, 10:06, 14:44, 18:53"},
        {service: "82 & 87", times: "05:35, 10:32, 15:15, 19:22"},
        {service: "82 & 87", times: "05:55, 11:05, 15:54, 19:46"},
        {service: "82 & 87", times: "06:15, 11:35, 16:24, 20:33"},
        {service: "82 & 87", times: "06:45, 12:07, 16:54, 21:51"},
        {service: "82 & 87", times: "07:04, 12:37, 17:22, 22:43"},
        {service: "82 & 87", times: "07:19, 13:07, 17:56, 23:39"},
        {service: "82 & 87", times: "07:42, 13:37, 18:24"},
        {service: "82 & 87", times: "08:06, 14:09"},
        {service: "82 & 87", times: "08:38, 14:44"},
        {service: "82 & 87", times: "09:14, 15:15"}
    ]
};

document.addEventListener("DOMContentLoaded", () => {
    const stopHeading = document.querySelector('header h1');
    if (!stopHeading) return;
    
    const currentStopName = stopHeading.textContent.trim();

    const schedule = stopSchedules[currentStopName];
    
    if (schedule) {
        renderStopTimetable(schedule);
    } else {
        console.warn(`No schedule data found for stop: "${currentStopName}"`);
    }
});

function renderStopTimetable(scheduleData) {
    const tableBody = document.querySelector('.timetable tbody');
    if (!tableBody) return;

    tableBody.innerHTML = ''; 

    scheduleData.forEach(row => {
        const tr = document.createElement('tr');

        const serviceCell = document.createElement('td');
        serviceCell.textContent = row.service;

        const timesCell = document.createElement('td');
        timesCell.textContent = row.times;

        tr.appendChild(serviceCell);
        tr.appendChild(timesCell);
        tableBody.appendChild(tr);
    });
}