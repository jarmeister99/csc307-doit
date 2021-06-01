import { Calendar, momentLocalizer } from 'react-big-calendar'
import style from 'react-big-calendar/lib/css/react-big-calendar.css';
import moment from 'moment'
import React, { useState } from "react";
import "../index.css"
import events from "./events"

function MonthView() {

    const localizer = momentLocalizer(moment)
    return (
        <div className="col-md-3" style={{width: '50%', minWidth: 800, height: 500, marginLeft: 'auto', marginRight: 'auto',scale: '150%'}}>
            <Calendar
                localizer={localizer}
                showMultiDayTimes
                defaultDate={new Date(2021,6,1)}
                events={events}
                startAccessor="start"
                endAccessor="end"
                style={{style}}
                
            />
        </div>
    );


}

export default MonthView;